from marshmallow import Schema, fields, validate

from api.models import ProductType


class AvailableProductSchema(Schema):
    type = fields.Enum(ProductType, required=False, by_value=True, load_default=None)
    page_size = fields.Integer(
        required=True,
        validate=validate.Range(min=0, error="pageSize must be positive"),
        data_key="pageSize",
    )


class ProductSchema(Schema):
    id = fields.Integer(required=False, strict=True)
    type = fields.Enum(ProductType, required=True, by_value=True)
    name = fields.String(required=True)
    inventory = fields.Integer(required=True, strict=True)
    desription = fields.String(required=False)


class OrderSchema(Schema):
    productid = fields.Integer(required=True, strict=True)
    count = fields.Integer(required=True, strict=True)
    status = fields.Constant("pending", load_only=True)
