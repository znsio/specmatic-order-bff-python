import pytest
from specmatic.core.specmatic import Specmatic
from specmatic.coverage.servers.flask_app_coverage_server import FlaskAppCoverageServer
from specmatic.servers.wsgi_app_server import WSGIAppServer

from api import app
from definitions import ROOT_DIR
from test import expectation_json_files

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
app_server = WSGIAppServer(app, app_host, app_port)
coverage_server = FlaskAppCoverageServer(app)

app_server.start()
coverage_server.start()


class TestContract:
    pass


Specmatic().with_project_root(ROOT_DIR).with_stub(stub_host, stub_port, expectation_json_files).with_endpoints_api(
    coverage_server.endpoints_api,
).test(TestContract, app_host, app_port).run()

app_server.stop()
coverage_server.stop()

if __name__ == "__main__":
    pytest.main()
