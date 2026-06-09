import yaml
from api_test_toolkit.models import Suite
from pathlib import Path

def load_suite(path: Path) -> Suite:
    with open(path, "r", encoding="utf-8") as f:
        file_data = f.read()

    data = yaml.safe_load(file_data)

    suite_data = Suite.model_validate(data)
    return suite_data