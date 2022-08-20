"""Fixtures are a potential and common use of `conftest.py`.

The fixtures defined here will be shared among tests in your test suite.

See Also:
    https://docs.pytest.org/en/latest/reference/fixtures.html?highlight=conftest#conftest-py-sharing-fixtures-across-multiple-files # noqa: E501

"""
# Standard Library
import os
import sys

# 3rd Party Libraries
import pytest


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
for _ in ("../", "../secrets_updater"):
    sys.path.insert(0, os.path.abspath(f"{BASE_DIR}/{_}"))

# Project Libraries
from secrets_updater.github import GitHubActions  # noqa: E402


@pytest.fixture(scope="function")
def get_public_key_details():
    return {"key": "abcdedfs1232", "key_id": "12345678"}


@pytest.fixture(scope="function")
def get_githubactions(get_public_key_details):
    def _get_githubactions(with_public_key=False):
        if with_public_key:
            return GitHubActions(
                public_key=get_public_key_details.get("key"),
                public_key_id=get_public_key_details.get("key_id"),
            )
        return GitHubActions()

    return _get_githubactions


@pytest.fixture(scope="function")
def secrete_file_content():
    data = "SECRET_1=Some random value 1\nSECRET_2=Some random value 2"
    return {
        "data": data,
        "items": (
            ("SECRET_1", "Some random value 1"),
            ("SECRET_2", "Some random value 2"),
        ),
    }


@pytest.fixture
def get_secretes_file(mocker, secrete_file_content):
    mocked_data = mocker.mock_open(read_data=secrete_file_content.get("data"))
    mocker.patch("builtins.open", mocked_data)
