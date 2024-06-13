"""Init for cleanups."""

from .database import close_db, init_db

__all__ = ["init_db", "close_db"]
