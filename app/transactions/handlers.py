"""Handlers transactions."""

from datetime import datetime

from aiohttp import web

from app.db.models import Transaction, User


async def create_user(request):
    """Create user."""
    data = await request.json()
    user = await User.create(name=data["name"])
    return web.json_response({"id": user.id, "name": user.name}, status=201)


async def add_transaction(request):
    """Add transaction."""
    data = await request.json()
    user_id = data["user_id"]
    amount = data["amount"]
    type = data["type"]
    uid = data["uid"]
    timestamp = data.get("timestamp", datetime.utcnow().isoformat())

    user = await User.get(user_id)
    if not user:
        return web.json_response({"error": "User not found"}, status=404)

    if type == "WITHDRAW" and user.balance < amount:
        return web.json_response({"error": "Insufficient funds"}, status=402)

    new_balance = user.balance + amount if type == "DEPOSIT" else user.balance - amount

    await user.update(balance=new_balance).apply()
    transaction = await Transaction.create(user_id=user_id, amount=amount, type=type, id=uid, timestamp=timestamp)

    return web.json_response({"transaction_id": transaction.id})


async def get_transaction(request):
    """Get transaction."""
    transaction_id = request.match_info["id"]
    transaction = await Transaction.get(transaction_id)
    if not transaction:
        return web.json_response({"error": "Transaction not found"}, status=404)
    return web.json_response(
        {
            "id": transaction.id,
            "user_id": transaction.user_id,
            "type": transaction.type,
            "amount": transaction.amount,
            "timestamp": transaction.timestamp.isoformat(),
        }
    )


async def get_user_balance(request):
    """Get user balance."""
    user_id = request.match_info["id"]
    date = request.query.get("date")
    user = await User.get(user_id)
    if not user:
        return web.json_response({"error": "User not found"}, status=404)

    if date:
        transactions = (
            await Transaction.query.where(Transaction.user_id == user_id)
            .where(Transaction.timestamp <= date)
            .gino.all()
        )
        balance = sum(txn.amount if txn.type == "DEPOSIT" else -txn.amount for txn in transactions)
    else:
        balance = user.balance

    return web.json_response({"balance": str(balance)})
