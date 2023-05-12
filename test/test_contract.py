import pytest

from specmatic_python.specmatic.decorators import start_flask_app, specmatic_stub, specmatic_contract_test
from api import app
from definitions import ROOT_DIR

host = "127.0.0.1"
port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
specmatic_json_file = ROOT_DIR + '/specmatic.json'
expectation_json_file = ROOT_DIR + '/test/data/expectation.json'


@specmatic_contract_test(host, port)
@specmatic_stub(stub_host, stub_port, [expectation_json_file])
@start_flask_app(app, host, port)
class TestApiContract:
    @classmethod
    def teardown_class(cls):
        cls.flask_server.stop()
        cls.stub.stop()


if __name__ == '__main__':
    pytest.main()
