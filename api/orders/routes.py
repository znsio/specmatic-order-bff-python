from typing import TYPE_CHECKING

from flask import Blueprint, jsonify, request

from api.schemas import OrderSchema
from api.services import OrdersService

if TYPE_CHECKING:
    from api.models import Order

orders = Blueprint("orders", __name__)
order_schema = OrderSchema()


@orders.route("/orders", methods=["POST"])
def create_order():
    data: Order = order_schema.load(request.json)  # type: ignore[reportAssignmentType]
    order = OrdersService.create_order(data)
    return jsonify(id=order["id"]), 201
