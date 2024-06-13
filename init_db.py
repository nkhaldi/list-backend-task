"""Init db."""

import asyncio

from app.config import Config
from app.db.database import db


async def run_init_db():
    """Run init db."""
    await db.set_bind(Config.DATABASE_URI)
    db.create_all()


if __name__ == "__main__":
    asyncio.run(run_init_db())
