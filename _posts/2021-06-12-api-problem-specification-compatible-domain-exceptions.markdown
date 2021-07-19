---
layout: post
title:  "API-Problem Specification Compatible Domain Exceptions"
description: "Making your domain exceptions work with your api problem library<br/>(RFC7807 Problem Details for HTTP APIs)"
date: 2021-06-12
tags: [Joy of Coding, English]
categories: [Joy of Coding]
reading_time: "10 min."
---


RFC7807 Problem Details Specification "defines a 'problem detail' as a way to carry machine-readable details of errors in a HTTP response to avoid the need to define new error response formats for HTTP APIs." <sup>[[1]](#references-1)</sup>

If you don't know the API-Problem Specification and/or want to learn more about it, you can read this article by Guy Levin: [REST API Error Handling - Problem Details Response](https://blog.restcase.com/rest-api-error-handling-problem-details-response/){:target="_blank"} 

In this article, I try to cover how I handle domain exceptions and return api problem formatted http response in a [Mezzio](https://docs.mezzio.dev/){:target="_blank"} app, but you will get the general idea.

Mezzio enables you to create middleware applications. A middleware is executed between request and response, and accepts a request object and returns a response object.

Typical middleware stack with handling api-problem details is shown below.


{% highlight php linenos %}

<?php

declare(strict_types=1);

use Mezzio\Application;
use Mezzio\MiddlewareFactory;
use Psr\Container\ContainerInterface;
use Mezzio\ProblemDetails\ProblemDetailsMiddleware;
use Mezzio\Router\Middleware\DispatchMiddleware;
use Mezzio\Router\Middleware\RouteMiddleware;
use Mezzio\Handler\NotFoundHandler;


return static function (Application $app, MiddlewareFactory $factory, ContainerInterface $container) : void {

    $app->pipe(ProblemDetailsMiddleware::class);
    ...
    $app->pipe(RouteMiddleware::class);
    ...
    $app->pipe(DispatchMiddleware::class);
    ...
    $app->pipe(NotFoundHandler::class);
};


{% endhighlight %}

In this stack, [ProblemDetailsMiddleware](https://docs.mezzio.dev/mezzio-problem-details/){:target="_blank"} provides a middleware that catches the last thrown exception and returns JSON error response that implements API-Problem Specification.

Let's say an endpoint accepts an email and stores it, but email is not a valid email address, then throws InvalidArgumentException. With ProblemDetailsMiddleware, response is like this.

{% highlight php linenos %}

throw new \InvalidArgumentException(sprintf('Email is not a valid email address: %s', $payload['email']), 400);

{% endhighlight %}


{% highlight json linenos %}
{
  "exception": {
    "class": "InvalidArgumentException",
    "code": 400,
    "message": "Email is not a valid email address: mehmet@mkorkmaz.com",
    "file": "/opt/app/src/Infrastructure/Ui/PrivateApi/IdentityAndAccess/Handler/RegisterAccount.php",
    "line": 47,
    "trace": [
        ...
    ]
  },
  "title": "Bad Request",
  "type": "https://httpstatus.es/400",
  "status": 400,
  "detail": "Email is not a valid email address: mehmet@mkorkmaz.com"

{% endhighlight %}


But I have problems with this output.

* HTTP status code is set using thrown exception's code, but I need different status code and error code. i.e. I want to return "404" as HTTP status and "users/user-not-found" as error code, so an API client can use the "users/user-not-found" to implement multilingual warning messages.
* I want to set custom url for "type". For example: https://my-awesome-api-url.com/docs/errors/users/user-not-found
* I want to set "title". For example "User Not Found" instead of "Not Found".
* I want to provide "additional" data with it. For example {"rateLimit": 300, "totalRequestsLastHour": 128 }
* Since this response is for clients, I don't want to share some internal information in "trace" and other places. I can use an error handler to log this internal information, then return the api problem error response.


Since in my "domain code" I throw lots of informative exceptions and I want my error responses use these informations.

ProblemDetailsMiddleware provides a trait named CommonProblemDetailsExceptionTrait but it only handles exception internal data to api problem error response data transformation. I need an another trait that helps to create an exception and use its internal data for api problem error responses.

Then I created a trait named DomainException.


{% highlight php linenos %}

<?php

declare(strict_types=1);

namespace MyApplication\Domain\Shared\Exception;

use Mezzio\ProblemDetails\Exception\CommonProblemDetailsExceptionTrait;

use function array_merge;
use function defined;

trait DomainException
{
    use CommonProblemDetailsExceptionTrait;

    private function __construct(int $status, string $detail, string $title, string $type, array $additional)
    {
        $this->status     = $status;
        $this->detail     = $detail;
        $this->title      = $title;
        $this->type       = $type;
        $this->additional = $additional;
        parent::__construct($detail, $status);
    }

    public static function create(string $details, ?array $additional = []): self
    {
        return new static(
            self::STATUS,
            $details,
            self::TITLE,
            defined('static::TYPE') ? self::TYPE : 'https://httpstatus.es/' . self::STATUS,
            array_merge($additional, ['code' => self::CODE])
        );
    }
}


{% endhighlight %}

Then I am enabled to define my domain exceptions.

{% highlight php linenos %}

<?php

declare(strict_types=1);

namespace MyApplication\Domain\Administrators\Exception;

use Mezzio\ProblemDetails\Exception\ProblemDetailsExceptionInterface;
use Exception;
use MyApplication\Domain\Shared\Exception\DomainException;

class UserNotFound extends Exception implements ProblemDetailsExceptionInterface
{
    use DomainException;

    private const STATUS = 404;
    private const CODE   = 'users/user-not-found';
    private const TYPE   = 'https://my-awesome-api-url.com/docs/errors/users/user-not-found';
    private const TITLE  = 'User Not Found';
}

{% endhighlight %}


Using this exception, my hypothetical final code is completed.

{% highlight php linenos %}
<?php

...

use MyApplication\Domain\Administrators\Exception\UserNotFound;

...

$message = new AuthenticateUserWithEmail($payload['email'], $payload['password']);

$user = $this->queryBus->handle($message);

if ($user === null) {
    $message = sprintf(
        'Invalid username and/or password for: %s', 
        $payload['email']
    );
    $additionalData = [
        'rateLimit'             => 10,
        'totalRequestsLast15Minutes' => 7
    ];
    throw UserNotFound::create($message, $additionalData);
}

...

{% endhighlight %}

And the result is:

{% highlight json linenos %}

{
  "rateLimit": 10,
  "totalRequestsLast15Minutes": 7,
  "code": "users/user-not-found",
  "title": "User Not Found",
  "type": "https://my-awesome-api-url.com/docs/errors/users/user-not-found",
  "status": 404,
  "detail": "Invalid username and/or password for mehmet@mkorkmaz.com"
}
{% endhighlight %}


If you have questions and suggestions, or find bugs in code and logic, please contact me.

<hr/>

#### References

<a name="references-1">[1]</a> [RFC7807 Problem Details Specification](https://datatracker.ietf.org/doc/html/rfc7807){:target="_blank"}



