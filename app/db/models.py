"""Database models."""

from datetime import datetime

from gino import Gino
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String

db = Gino()


class User(db.Model):
    """User model."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    balance = Column(Numeric, default=0)


class Transaction(db.Model):
    """Transaction model."""

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String(10))  # DEPOSIT or WITHDRAW
    amount = Column(Numeric)
    timestamp = Column(DateTime, default=datetime.utcnow)
