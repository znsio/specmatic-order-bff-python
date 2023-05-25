import pytest
from api import app
from definitions import ROOT_DIR
from specmatic.core.specmatic import Specmatic

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
expectation_json_file = ROOT_DIR + '/test/data/expectation.json'
service_contract_file = ROOT_DIR + '/test/spec/product-search-bff-api.yaml'
stub_contract_file = ROOT_DIR + '/test/spec/api_order_v1.yaml'


class TestContract:
    pass


stub = None
app_server = None

try:
    stub = Specmatic.start_stub(ROOT_DIR, stub_host, stub_port, '', stub_contract_file)
    stub.set_expectations([expectation_json_file])

    app_server = Specmatic.start_wsgi_app(app, app_host, app_port)

    Specmatic.test(ROOT_DIR, TestContract, app_host, app_port, '', service_contract_file)
except Exception as e:
    print(f"Error: {e}")
    raise e
finally:
    if app_server is not None:
        app_server.stop()
    if stub is not None:
        stub.stop()

if __name__ == '__main__':
    pytest.main()
