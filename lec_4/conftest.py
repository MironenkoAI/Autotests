from datetime import datetime

import pytest
import yaml


with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture(autouse=True)
def print_time():
    print("Start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
    yield
    print("Finish: {}".format(datetime.now().strftime("%H:%M:%S.%f")))