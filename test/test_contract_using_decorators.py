import pytest

from specmatic.core.decorators import specmatic_contract_test, specmatic_stub, start_app
from api import app
from definitions import ROOT_DIR

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
expectation_json_file = ROOT_DIR + '/test/data/expectation.json'
service_contract_file = ROOT_DIR + '/test/spec/product-search-bff-api.yaml'
stub_contract_file = ROOT_DIR + '/test/spec/api_order_v1.yaml'


@specmatic_contract_test(ROOT_DIR, app_host, app_port, service_contract_file)
@start_app(app, app_host, app_port)
@specmatic_stub(ROOT_DIR, stub_host, stub_port, [expectation_json_file], stub_contract_file)
class TestContractWithLocalSpecs:
    pass


if __name__ == '__main__':
    pytest.main()
