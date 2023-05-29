import pytest
from api import app
from definitions import ROOT_DIR
from specmatic.core.specmatic import Specmatic

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
expectation_json_file = ROOT_DIR + '/test/data/expectation.json'
app_contract_file = ROOT_DIR + '/test/spec/product-search-bff-api.yaml'
stub_contract_file = ROOT_DIR + '/test/spec/api_order_v1.yaml'


class TestContract:
    pass


Specmatic.test_wsgi_app(app,
                        TestContract,
                        app_contracts=[app_contract_file],
                        stub_contracts=[stub_contract_file],
                        app_host=app_host,
                        app_port=app_port,
                        stub_host=stub_host,
                        stub_port=stub_port,
                        expectation_files=[expectation_json_file])

if __name__ == '__main__':
    pytest.main()
