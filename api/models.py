import enum
from typing import TypedDict


class ProductType(str, enum.Enum):
    GADGET = "gadget"
    BOOK = "book"
    FOOD = "food"
    OTHER = "other"


class AvailableProductType(TypedDict):
    type: ProductType | None
    page_size: int


class Product(TypedDict):
    name: str
    type: ProductType
    inventory: int
    desription: str | None


class Order(TypedDict):
    status: str
    productid: int
    count: int
