"""Preview the static site with GitHub Pages-style extensionless HTML URLs."""

import argparse
from functools import partial
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
ASSET_EXTENSIONS = {".css", ".js", ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".woff", ".woff2", ".ttf", ".otf", ".eot"}


def resolvePublishedFile(directory, requestPath):
    root = Path(directory).resolve()
    route = unquote(urlsplit(requestPath).path)
    parts = route.strip("/").split("/")
    if any(part.startswith((".", "_")) or part in {"drafts", "test", "tools"} for part in parts):
        return None
    candidate = (root / (route.lstrip("/") or "index.html")).resolve()
    if root not in candidate.parents:
        return None
    if not candidate.suffix:
        candidate = candidate.with_suffix(".html")
    if not candidate.is_file():
        return None
    if candidate.suffix == ".html":
        return candidate
    if candidate.parent == root and candidate.name in {"feed.xml", "sitemap.xml", "robots.txt"}:
        return candidate
    if candidate.is_relative_to(root / "assets") and candidate.suffix.lower() in ASSET_EXTENSIONS:
        return candidate
    return None


class StaticSiteHandler(SimpleHTTPRequestHandler):
    def sendFile(self, path, status):
        document = path.open("rb")
        self.send_response(status)
        self.send_header("Content-Type", self.guess_type(str(path)))
        self.send_header("Content-Length", str(path.stat().st_size))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        return document

    def send_head(self):
        path = resolvePublishedFile(self.directory, self.path)
        if path is None:
            self.send_error(HTTPStatus.NOT_FOUND)
            return None
        return self.sendFile(path, HTTPStatus.OK)

    def send_error(self, code, message=None, explain=None):
        if code != HTTPStatus.NOT_FOUND:
            return super().send_error(code, message, explain)
        with self.sendFile(Path(self.directory) / "404.html", HTTPStatus.NOT_FOUND) as document:
            if self.command != "HEAD":
                self.copyfile(document, self.wfile)


def main():
    argumentParser = argparse.ArgumentParser(description=__doc__)
    argumentParser.add_argument("--port", type=int, default=4000)
    arguments = argumentParser.parse_args()
    handler = partial(StaticSiteHandler, directory=str(ROOT))
    with ThreadingHTTPServer(("127.0.0.1", arguments.port), handler) as server:
        print(f"Static site: http://127.0.0.1:{arguments.port}/", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nPreview stopped.")


if __name__ == "__main__":
    main()
