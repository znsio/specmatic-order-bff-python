import os
import pathlib

from api import app
from definitions import ROOT_DIR

expectation_json_files = []
for file in pathlib.Path(ROOT_DIR, "test/data").iterdir():
    if file.is_file() and file.suffix == ".json":
        expectation_json_files.append(file.absolute())  # noqa: PERF401


APP_HOST = "127.0.0.1"
APP_PORT = 5000
STUB_HOST = "127.0.0.1"
STUB_PORT = 8080
APP = app

os.environ["SPECMATIC_GENERATIVE_TESTS"] = "true"
