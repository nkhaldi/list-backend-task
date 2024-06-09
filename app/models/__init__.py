"""Init for models."""

from gino import Gino

db = Gino()


class User(db.Model):
    """User model."""

    balance = db.Column(...)
    ...


class Transaction(db.Model):
    """Transaction model."""

    ...
