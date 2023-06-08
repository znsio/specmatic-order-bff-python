import os
import pytest
from specmatic.core.specmatic import Specmatic
from specmatic.servers.wsgi_app_server import WSGIAppServer
from api import app
from definitions import ROOT_DIR

expectation_json_file = ROOT_DIR + '/test/data/expectation.json'


class TestContract:
    pass


def update_app_config_with_stub_info(app, host: str, port: int):
    app.config['ORDER_API_HOST'] = host
    app.config['ORDER_API_PORT'] = str(port)


def reset_app_config(app):
    app.config["ORDER_API_HOST"] = os.getenv("ORDER_API_HOST")
    app.config["ORDER_API_PORT"] = os.getenv("ORDER_API_PORT")


app_server = WSGIAppServer(app, set_app_config_func=update_app_config_with_stub_info,
                           reset_app_config_func=reset_app_config)
Specmatic() \
    .with_project_root(ROOT_DIR) \
    .stub(expectations=[expectation_json_file]) \
    .app(app_server) \
    .test(TestContract) \
    .run()

reset_app_config(app)

if __name__ == '__main__':
    pytest.main()
