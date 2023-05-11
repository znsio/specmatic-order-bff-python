import requests


class Products:
    products_api = 'http://127.0.0.1:8080/products'

    def search(self, product_type: str):
        return requests.get(self.products_api, params={'type': product_type})
