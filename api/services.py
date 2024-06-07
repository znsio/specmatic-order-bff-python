from typing import ClassVar

import requests
from flask import abort

from api import app
from api.models import Order, Product, ProductType
from api.schemas import ProductSchema


class ProductService:
    _AUTH_TOKEN = "API-TOKEN-SPEC"  # noqa: S105
    _TIMEOUT: int = app.config["REQ_TIMEOUT"]
    _API_URL = f"http://{app.config['ORDER_API_HOST']}:{app.config['ORDER_API_PORT']}"
    _API_LIST: ClassVar[dict[str, str]] = {
        "SEARCH": "/products",
        "CREATE": "/products",
    }
    _prod_schema = ProductSchema()

    @staticmethod
    def find_products(p_type: ProductType | None) -> list[Product]:
        # NOTE: ORDER_API_PORT needs to react to autowiring test app.config changes
        ProductService._API_URL = f"http://{app.config['ORDER_API_HOST']}:{app.config['ORDER_API_PORT']}"
        resp = requests.get(
            f"{ProductService._API_URL}{ProductService._API_LIST['SEARCH']}",
            params={"type": p_type.value if p_type else None},
            timeout=ProductService._TIMEOUT,
        )
        if resp.status_code != 200:
            return abort(resp.status_code, "An error occurred while retrieving the products.")

        return ProductService._prod_schema.loads(resp.text, many=True)  # type: ignore[return-value]

    @staticmethod
    def create_product(product: Product) -> dict[str, int]:
        # NOTE: ORDER_API_PORT needs to react to autowiring test app.config changes
        ProductService._API_URL = f"http://{app.config['ORDER_API_HOST']}:{app.config['ORDER_API_PORT']}"
        resp = requests.post(
            f"{ProductService._API_URL}{ProductService._API_LIST['CREATE']}",
            json=product,
            headers={"Authenticate": ProductService._AUTH_TOKEN},
            timeout=ProductService._TIMEOUT,
        )

        if resp.status_code != 200:
            return abort(resp.status_code, "An error occurred while creating the product.")

        return resp.json()


class OrdersService:
    _AUTH_TOKEN = "API-TOKEN-SPEC"  # noqa: S105
    _TIMEOUT: int = app.config["REQ_TIMEOUT"]
    _API_URL = f"http://{app.config['ORDER_API_HOST']}:{app.config['ORDER_API_PORT']}"
    _API_LIST: ClassVar[dict[str, str]] = {
        "CREATE": "/orders",
    }

    @staticmethod
    def create_order(order: Order) -> dict[str, int]:
        # NOTE: ORDER_API_PORT needs to react to autowiring test app.config changes
        OrdersService._API_URL = f"http://{app.config['ORDER_API_HOST']}:{app.config['ORDER_API_PORT']}"
        resp = requests.post(
            f"{OrdersService._API_URL}{OrdersService._API_LIST['CREATE']}",
            json=order,
            headers={"Authenticate": OrdersService._AUTH_TOKEN},
            timeout=OrdersService._TIMEOUT,
        )

        if resp.status_code != 200:
            return abort(resp.status_code, "An error occurred while creating the order.")

        return resp.json()
