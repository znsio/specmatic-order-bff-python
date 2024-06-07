import pytest
from specmatic.core.decorators import (
    specmatic_contract_test,
    specmatic_stub,
    start_wsgi_app,
)

from api import app
from definitions import ROOT_DIR
from test import expectation_json_files

host = "127.0.0.1"
port = 5000
stub_host = "127.0.0.1"
stub_port = 8080


@specmatic_contract_test(host, port, ROOT_DIR)  # type: ignore[reportArgumentType]
@start_wsgi_app(app, host, port)
@specmatic_stub(stub_host, stub_port, str(ROOT_DIR), expectation_json_files)
class TestApiContract:
    pass


if __name__ == "__main__":
    pytest.main()
