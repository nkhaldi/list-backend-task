"""Main module for app."""

import uvloop
from aiohttp import web

from app.app import init_app


def create_app() -> web.Application:
    """Create app."""
    app = init_app()
    return app


def main() -> None:
    """Run app."""
    uvloop.install()
    app = init_app()
    web.run_app(app, host=app["config"].HOST, port=app["config"].PORT)


if __name__ == "__main__":
    main()
