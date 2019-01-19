---
layout: post
title:  "ReJSON-PHP"
description: "PHP Client for ReJSON by Redislabs"
date:   2018-12-23 00:48:45 +0300
tags: [Joy Of Coding, English]
categories: [Joy of Coding]
---

ReJSON-PHP is PHP Client for Redislabs' ReJSON Module. It supports both widely used redis clients for PHP (PECL Redis Extension and Predis).

To try ReJSON you can use Docker Image provided by Redislabs.

```sh
docker run -p 6379:6379 redislabs/rejson:latest
```

You will need PECL Redis Extension or Predis to use ReJSON-PHP. The recommended method to installing ReJSON-PHP is with composer.

```sh
php composer require mkorkmaz/redislabs-rejson
```

```php
<?php
declare(strict_types=1);

use Redis;
use Redislabs\Module\ReJSON\ReJSON;

$redisClient = new Redis();
$redisClient->connect('127.0.0.1');
$reJSON = ReJSON::createWithPhpRedis($redisClient);

$reJSON->set('test', '.', ['foo'=>'bar'], 'NX');
$reJSON->set('test', '.baz', 'qux');
$reJSON->set('test', '.baz', 'quux', 'XX');
$baz = $reJSON->get('test', '.baz');
```