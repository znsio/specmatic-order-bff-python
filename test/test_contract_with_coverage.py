import pytest
from specmatic.core.specmatic import Specmatic

from api import app
from definitions import ROOT_DIR
from test import expectation_json_files

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080


class TestContract:
    pass


Specmatic().with_project_root(ROOT_DIR).with_stub(stub_host, stub_port, expectation_json_files).with_wsgi_app(
    app,
    app_host,
    app_port,
).test_with_api_coverage_for_flask_app(TestContract, app).run()

if __name__ == "__main__":
    pytest.main()
