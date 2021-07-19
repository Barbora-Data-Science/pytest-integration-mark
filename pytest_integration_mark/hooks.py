"""Pytest hooks to add required marks for integration tests and apply filtering logic."""

from pathlib import Path
from typing import List

import pytest
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.nodes import Item

INTEGRATION_MARK = "integration"


def pytest_configure(config: Config) -> None:
    """Registers the integration test mark.

    Args:
        config: pytest configuration.
    """
    config.addinivalue_line(
        "markers",
        f"{INTEGRATION_MARK}: mark a test as an integration test (slow, requires test database).",
    )


def pytest_collection_modifyitems(config: Config, items: List[Item]) -> None:
    """Marks tests in the integration folder as integration tests (which will not run by default).

    Args:
        config: pytest configuration.
        items: Items to test (individual tests).
    """
    integration_folder = config.getoption("--integration-tests-folder")
    root_dir = Path(config.rootdir)
    test_paths = ((test_item, Path(test_item.fspath)) for test_item in items)
    integration_tests = (
        test_item
        for test_item, test_path in test_paths
        if root_dir / integration_folder in test_path.parents
    )
    mark = getattr(pytest.mark, INTEGRATION_MARK)
    for test_item in integration_tests:
        test_item.add_marker(mark)


def pytest_addoption(parser: Parser) -> None:
    """Adds custom options to specific to integration tests (disabled by default).

    Args:
        parser: pytest's command line argument parser to add options to.
    """
    parser.addoption(
        "--with-integration", action="store_true", help="run integration tests as well"
    )
    parser.addoption(
        "--integration-tests-folder",
        type=Path,
        default=Path("tests/integration"),
        help="folder where all tests which should be marked as integration tests reside relative "
        "to test root folder (default: %default)",
    )


def pytest_runtest_setup(item: Item) -> None:
    """Do not run tests marked as integration tests by default, unless a flag is set.

    Args:
        item: pytest's test item.
    """
    if INTEGRATION_MARK in item.keywords and not item.config.getoption(
        "--with-integration"
    ):
        pytest.skip("pass --with-integration to run integration tests")
