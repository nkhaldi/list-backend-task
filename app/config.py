"""Config."""

import os


class Config:
    """Config."""

    DEBUG = os.getenv("DEBUG", False)
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    DATABASE_URI = os.getenv("DATABASE_URI", "postgres://postgres:postgres@db:5432/postgres")
