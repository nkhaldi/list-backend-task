"""Routes for API."""

from aiohttp.web import Application, json_response

from app.transactions.handlers import add_transaction, create_user, get_transaction, get_user_balance


async def root(request):
    """Root route."""
    return json_response({"status": "ok"})


def add_routes(app: Application):
    """Add routes."""
    app.router.add_route("GET", r"/", root, name="root")
    app.router.add_route("POST", r"/v1/user", create_user, name="create_user")
    app.router.add_route("POST", r"/v1/transaction", add_transaction, name="add_transaction")
    app.router.add_route("GET", r"/v1/transaction/{id}", get_transaction, name="get_transaction")
    app.router.add_route("GET", r"/v1/user/{id}", get_user_balance, name="get_user_balance")
