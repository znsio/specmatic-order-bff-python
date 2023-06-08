import pytest
from api import app
from definitions import ROOT_DIR
from specmatic.core.specmatic import Specmatic
from specmatic.servers.wsgi_app_server import WSGIAppServer

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
expectation_json_file = ROOT_DIR + '/test/data/expectation.json'


class TestContract:
    pass


app_server = WSGIAppServer(app, app_host, app_port)
Specmatic() \
    .with_project_root(ROOT_DIR) \
    .stub(stub_host, stub_port, [expectation_json_file]) \
    .app(app_server) \
    .test(TestContract) \
    .run()

if __name__ == '__main__':
    pytest.main()
