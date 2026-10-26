"""Check the exported pages and their public URL contracts without Jekyll."""

from functools import partial
from html.parser import HTMLParser
from http.server import ThreadingHTTPServer
from threading import Thread
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlsplit
from urllib.request import Request, urlopen
import re
import unittest
import xml.etree.ElementTree as ElementTree

from serve import ROOT, StaticSiteHandler, resolvePublishedFile


BLOG_ROUTES = [
    "/2021/06/api-problem-specification-compatible-domain-exceptions",
    "/2019/03/bedavaya-calismali-miyim",
    "/2019/03/belirsizligi-yonetmek-kimin-gorevidir",
    "/2019/03/degisime-acik-olmak",
    "/2016/03/remote-calisma-ne-kadar-mumkun",
    "/2012/06/memsql-at-first-sight-promising-mysql-replacement",
    "/2011/09/programming-in-the-cloud",
]
JOURNAL_ROUTES = [
    "/2026/10/mcgregordan-gunumuze-yapay-zeka-caginda-hayatin-insani-yonu",
]
ARTICLE_ROUTES = JOURNAL_ROUTES + BLOG_ROUTES
PAGE_ROUTES = ["/", "/journal", "/blog", "/contact", "/joy-of-coding", "/agile-johnny", "/404"]
REDIRECT_ROUTES = {
    "/about": "/",
    "/2026/10/mcgregordan-gunumuze-yapay-zeka-caginda-hayatin-insan-yonu": JOURNAL_ROUTES[0],
}


class PageDocument(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.elements = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attributes):
        self.elements.append((tag, dict(attributes)))

    def select(self, tag, **attributes):
        return [values for name, values in self.elements if name == tag and all(values.get(key) == value for key, value in attributes.items())]


class QuietHandler(StaticSiteHandler):
    def log_message(self, format, *arguments):
        pass


class StaticSiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_routes_preserve_the_original_addresses_and_metadata(self):
        for route in PAGE_ROUTES + ARTICLE_ROUTES + list(REDIRECT_ROUTES):
            with self.subTest(route=route):
                path = resolvePublishedFile(ROOT, route)
                self.assertIsNotNone(path)
                document = PageDocument(path)
                canonicalRoute = REDIRECT_ROUTES.get(route, route)
                self.assertEqual([{"rel": "canonical", "href": "https://mkorkmaz.com" + canonicalRoute}], document.select("link", rel="canonical"))
                language = "tr" if route.startswith("/20") and route != BLOG_ROUTES[0] else "en"
                self.assertEqual(language, document.select("html")[0]["lang"])
                if route in REDIRECT_ROUTES:
                    self.assertEqual([{"http-equiv": "refresh", "content": "0; url=" + canonicalRoute}], document.select("meta", **{"http-equiv": "refresh"}))
                    self.assertEqual(1, len(document.select("a", href=canonicalRoute)))
                address = f"http://127.0.0.1:{self.server.server_port}{route}"
                with urlopen(address, timeout=5) as response:
                    self.assertEqual(200, response.status)
                    self.assertEqual(address, response.url)
                    self.assertEqual(path.read_bytes(), response.read())

    def test_all_pages_are_complete_html_without_template_processing(self):
        self.assertEqual(len(PAGE_ROUTES + ARTICLE_ROUTES) + len(REDIRECT_ROUTES), len(list(ROOT.glob("*.html"))) + len(list(ROOT.glob("20*/*/*.html"))))
        for route in PAGE_ROUTES + ARTICLE_ROUTES + list(REDIRECT_ROUTES):
            path = resolvePublishedFile(ROOT, route)
            source = path.read_text()
            self.assertTrue(source.startswith("<!DOCTYPE html>"), path)
            self.assertNotIn("{%", source)
            self.assertNotIn("{{", source)
            document = PageDocument(path)
            identifiers = [values["id"] for _, values in document.elements if "id" in values]
            self.assertEqual(len(identifiers), len(set(identifiers)), path)
            self.assertTrue(all("alt" in values for values in document.select("img")), path)

    def test_internal_navigation_and_assets_resolve(self):
        for route in PAGE_ROUTES + ARTICLE_ROUTES + list(REDIRECT_ROUTES):
            document = PageDocument(resolvePublishedFile(ROOT, route))
            for _, attributes in document.elements:
                for name in ("href", "src"):
                    target = attributes.get(name, "")
                    if target.startswith("/") and not target.startswith("//"):
                        self.assertIsNotNone(resolvePublishedFile(ROOT, target), f"{route}: {target}")
        source = (ROOT / "blog.html").read_text()
        positions = [source.index(f'href="{route}"') for route in BLOG_ROUTES]
        self.assertEqual(sorted(positions), positions)

    def test_homepage_biography_and_blog_navigation(self):
        home = (ROOT / "index.html").read_text()
        paragraphs = re.findall(r"<p>(.*?)</p>", home, re.DOTALL)
        self.assertEqual(5, len(paragraphs))
        self.assertIn("I am a product engineer", paragraphs[0])
        self.assertIn("My architectural approach", paragraphs[-1])
        self.assertEqual([], PageDocument(ROOT / "index.html").select("ul", id="post-list"))
        blog = PageDocument(ROOT / "blog.html")
        self.assertEqual(1, len(blog.select("ul", id="post-list")))
        self.assertEqual(BLOG_ROUTES, [link["href"] for link in blog.select("a") if link.get("href") in ARTICLE_ROUTES])
        for route in PAGE_ROUTES + ARTICLE_ROUTES:
            source = resolvePublishedFile(ROOT, route).read_text()
            expected = (["/"] if route != "/" else []) + ["/journal", "/blog", "/contact"]
            for pattern in (r'<nav class="device-lg main-nav">(.*?)</nav>', r'<ul id="mobile-menu" class="device-sm">(.*?)</ul>'):
                navigation = re.search(pattern, source, re.DOTALL).group(1)
                self.assertEqual(expected, re.findall(r'href="([^"]+)"', navigation), route)

    def test_journal_lists_its_articles_separately_from_blog(self):
        document = PageDocument(ROOT / "journal.html")
        self.assertEqual(1, len(document.select("ul", id="post-list")))
        self.assertEqual(JOURNAL_ROUTES, [link["href"] for link in document.select("a") if link.get("href") in ARTICLE_ROUTES])
        dates = [element["datetime"] for element in document.select("time")]
        self.assertEqual(len(JOURNAL_ROUTES), len(dates))
        self.assertEqual(sorted(dates, reverse=True), dates)
        self.assertIn("hidden", document.select("p", id="journal-empty")[0])
        for route in JOURNAL_ROUTES:
            article = PageDocument(resolvePublishedFile(ROOT, route))
            self.assertEqual(1, len(article.select("section", id="post-body")))
        blog = PageDocument(ROOT / "blog.html")
        self.assertEqual(BLOG_ROUTES, [link["href"] for link in blog.select("a") if link.get("href") in ARTICLE_ROUTES])

    def test_article_sharing_keeps_absolute_urls_and_complete_titles(self):
        for route in ARTICLE_ROUTES:
            document = PageDocument(resolvePublishedFile(ROOT, route))
            share = document.select("a", **{"class": "twitter"})[0]
            parameters = parse_qs(urlsplit(share["href"]).query)
            self.assertEqual(["https://mkorkmaz.com" + route], parameters["url"])
            self.assertEqual(["_mehmet_korkmaz"], parameters["via"])
            self.assertTrue(parameters["text"][0])
            self.assertEqual({"class", "href"}, set(share))
        remote = PageDocument(resolvePublishedFile(ROOT, BLOG_ROUTES[4]))
        self.assertIn('"Remote"', parse_qs(urlsplit(remote.select("a", **{"class": "twitter"})[0]["href"]).query)["text"][0])

    def test_feed_sitemap_and_contact_are_static(self):
        feed = ElementTree.parse(ROOT / "feed.xml")
        self.assertEqual("https://mkorkmaz.com/blog", feed.findtext("./channel/link"))
        self.assertEqual(BLOG_ROUTES, [urlsplit(item.text).path for item in feed.findall("./channel/item/link")])
        sitemap = ElementTree.parse(ROOT / "sitemap.xml")
        locations = sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        self.assertEqual(set(PAGE_ROUTES + ARTICLE_ROUTES), {urlsplit(item.text).path for item in locations})
        contact = PageDocument(ROOT / "contact.html")
        self.assertEqual([], contact.select("form"))
        self.assertEqual(1, len(contact.select("a", href="mailto:mehmet@mkorkmaz.com")))
        self.assertEqual("mkorkmaz.com", (ROOT / "CNAME").read_text().strip())
        self.assertEqual(b"", (ROOT / ".nojekyll").read_bytes())
        for name in ("Gemfile", "Gemfile.lock", "_config.yml", "index.md", "start.sh"):
            self.assertFalse((ROOT / name).exists(), name)

    def test_private_paths_and_unknown_routes_return_the_custom_404(self):
        for route in ("/unknown-page", "/drafts/a-draft-post.html", "/drafts/a-draft-post.markdown", "/_site/index.html", "/.git/config", "/README.md", "/test/site_test.rb", "/tools/serve.py", "/assets/../../drafts/a-draft-post.markdown"):
            with self.subTest(route=route):
                address = f"http://127.0.0.1:{self.server.server_port}{route}"
                with self.assertRaises(HTTPError) as result:
                    urlopen(address, timeout=5)
                with result.exception as response:
                    self.assertEqual(404, response.code)
                    self.assertEqual((ROOT / "404.html").read_bytes(), response.read())
        address = f"http://127.0.0.1:{self.server.server_port}{ARTICLE_ROUTES[0]}"
        with urlopen(Request(address, method="HEAD"), timeout=5) as response:
            self.assertEqual(200, response.status)
            self.assertEqual(b"", response.read())


if __name__ == "__main__":
    unittest.main()
