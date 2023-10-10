import pytest
import yaml
from checkout import checkout


with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folder():
    yield checkout(f'mkdir -p {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ext")}', '')
    checkout(f'rm -r {data.get("folder_in")} {data.get("folder_out")} {data.get("folder_ext")}', '')


@pytest.fixture()
def make_file():
    return checkout(f'cd {data.get("folder_in")}; touch file1.txt file2.txt file3.txt', '')