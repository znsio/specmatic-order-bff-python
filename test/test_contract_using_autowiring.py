import pytest
from specmatic.core.specmatic import Specmatic

from test import APP, ROOT_DIR, STUB_HOST, STUB_PORT, expectation_json_files


class TestContract:
    pass


def set_app_config(app, host: str, port: int):
    app.config["ORDER_API_HOST"] = host
    app.config["ORDER_API_PORT"] = str(port)
    app.config["API_URL"] = f"http://{host}:{port}"


def reset_app_config(app):
    app.config["ORDER_API_HOST"] = STUB_HOST
    app.config["ORDER_API_PORT"] = STUB_PORT
    app.config["API_URL"] = f"http://{STUB_HOST}:{STUB_PORT}"


Specmatic().with_project_root(ROOT_DIR).with_stub(expectations=expectation_json_files).with_wsgi_app(
    APP,
    set_app_config_func=set_app_config,
    reset_app_config_func=reset_app_config,
).test(TestContract).run()

reset_app_config(APP)

if __name__ == "__main__":
    pytest.main()
