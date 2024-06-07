import os

from definitions import ROOT_DIR

expectation_json_files = []
for root, _, files in os.walk(os.path.join(ROOT_DIR, "test/data")):  # noqa: PTH118
    for file in files:
        if file.endswith(".json"):
            expectation_json_files.append(os.path.join(root, file))  # noqa: PERF401, PTH118

os.environ["SPECMATIC_GENERATIVE_TESTS"] = "true"
