import pytest
from pathlib import Path

def pytest_collection_modifyitems(config, items):
    quarantine_file = Path("quarantine/quarantined_tests.txt")

    if quarantine_file.exists():
        quarantined = quarantine_file.read_text().splitlines()
    else:
        quarantined = []

    for item in items:
        test_name = item.nodeid

        if any(q in test_name for q in quarantined):
            item.add_marker(pytest.mark.quarantine)
            item.add_marker(pytest.mark.skip(reason="Test is quarantined due to flakiness"))