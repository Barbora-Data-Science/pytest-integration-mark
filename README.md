[![Formatter](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI version](https://badge.fury.io/py/pytest-integration-mark.svg)](https://pypi.org/project/pytest-integration-mark/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytest-integration-mark)](https://pypi.org/project/pytest-integration-mark/)


# Description
Provides a pytest marker `integration` for integration tests. 
This marker automatically applies to all tests in a specified integration test folder.
Integration tests will not run by default, which is useful for cases where an external dependency
needs to be set up first (such as a database service).

# Installation

This is a pure python package, so it can be installed with `pip install pytest-integration-mark` 
or any other dependency manager.

# Usage

After installation:

Running `pytest` as usual:
- Tests marked with `@pytest.mark.integration` will be skipped
- Tests in `./tests/integration/...` will be skipped

Running `pytest --with-integration`:
- Tests marked with `@pytest.mark.integration` will run
- Tests in `./tests/integration/...` will run

Running `pytest --with-integration --integration-tests-folder integration`:
- Tests marked with `@pytest.mark.integration` will run
- Tests in `./integration/...` will run

# Development

This library uses the [poetry](https://python-poetry.org/) package manager, which has to be installed before installing
other dependencies. Afterwards, run `poetry install` to create a virtualenv and install all dependencies.
To then activate that environment, use `poetry shell`. To run a command in the environment without activating it,
use `poetry run <command>`.

[Black](https://github.com/psf/black) is used (and enforced via workflows) to format all code. Poetry will install it
automatically, but running it is up to the user. To format the entire project, run `black .` inside the virtualenv.

# Contributing

This project uses the Apache 2.0 license and is maintained by the data science team @ Barbora. All contribution are 
welcome in the form of PRs or raised issues.
