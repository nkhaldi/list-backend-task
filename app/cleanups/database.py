"""Database cleanup functions."""

from aiohttp import web


async def close_db(app: web.Application) -> None:
    """Close database connection."""
    await app["db"].pop_bind().close()
