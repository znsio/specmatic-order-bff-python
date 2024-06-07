from typing import TYPE_CHECKING

from flask import Blueprint, abort, jsonify, request

from api.models import ProductType
from api.schemas import AvailableProductSchema, ProductSchema
from api.services import ProductService

if TYPE_CHECKING:
    from api.models import AvailableProductType, Product

products = Blueprint("products", __name__)
avail_prod_schema = AvailableProductSchema()
prod_schema = ProductSchema()


@products.route("/findAvailableProducts", methods=["GET"])
def find_available_products():
    args: AvailableProductType = avail_prod_schema.load(request.args | {"pageSize": request.headers.get("pageSize")})  # type: ignore[reportAssignmentType]

    # NOTE: API_SPEC v4 requires expects TIMEOUT when type="other" or pageSize=20
    if args.get("type") == ProductType.OTHER or args.get("page_size") == 20:
        return abort(503, "Timeout")

    products = ProductService.find_products(args.get("type"))
    return prod_schema.dump(products, many=True), 200


@products.route("/products", methods=["POST"])
def add_product():
    data: Product = prod_schema.load(request.json)  # type: ignore[reportAssignmentType]
    product = ProductService.create_product(data)
    return jsonify(id=product["id"]), 201
