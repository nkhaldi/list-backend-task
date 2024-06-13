"""App module."""

from aiohttp import web

from app.api.routes import add_routes
from app.config import Config
from app.db import close_db, init_db
from app.db.models import db

app = web.Application()
app["db"] = db


def init_app() -> web.Application:
    """Init app."""
    app["config"] = Config

    # Startups
    app.on_startup.append(init_db)

    # Cleanups
    app.on_cleanup.append(close_db)
    add_routes(app)

    return app
