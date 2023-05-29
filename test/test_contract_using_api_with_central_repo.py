import pytest
from specmatic.core.specmatic import Specmatic
from api import app
from definitions import ROOT_DIR

app_host = "127.0.0.1"
app_port = 5000
stub_host = "127.0.0.1"
stub_port = 8080
expectation_json_file = ROOT_DIR + '/test/data/expectation.json'


class TestContract:
    pass


Specmatic.test_wsgi_app(app,
                        TestContract,
                        project_root=ROOT_DIR,
                        stub_host=stub_host,
                        stub_port=stub_port,
                        expectation_files=[expectation_json_file])

if __name__ == '__main__':
    pytest.main()
