"""Test cases for `GitHubActions`."""
# Standard Library
from unittest.mock import patch

# 3rd Party Libraries
import pytest

# Project Libraries
from secrets_updater.settings import AUTH_HEADERS, REPO_PUBLIC_KEY_URL, SECRETS_URL


pytest_plugin = ("pytest_asyncio",)


@patch("requests.get")
def test_get_repo_secrets_success(patched_requests, get_githubactions):
    """Test if `get_repo_secrets` returns valid data."""
    response_data = {
        "total_count": 1,
        "secrets": [
            {
                "name": "GH_TOKEN",
                "created_at": "2019-08-10T14:59:22Z",
                "updated_at": "2020-01-10T14:59:22Z",
            }
        ],
    }

    patched_requests.return_value.status_code = 200
    patched_requests.return_value.json.return_value = response_data
    object = get_githubactions()
    response = object.get_repo_secrets()
    patched_requests.assert_called_with(SECRETS_URL, headers=AUTH_HEADERS)
    assert response_data == response


@patch("requests.get")
def test_get_repo_secrets_fail(patched_requests, get_githubactions):
    """Test if `get_repo_secrets` raises exception."""
    patched_requests.return_value.status_code = 400
    with pytest.raises(Exception):
        get_githubactions().get_repo_secrets()


@patch("requests.get")
def test_get_repo_public_key_success(
    patched_requests, get_githubactions, get_public_key_details
):
    """Test if `get_repo_public_key` returns valid data."""
    response_data = get_public_key_details

    patched_requests.return_value.status_code = 200
    patched_requests.return_value.json.return_value = response_data
    object = get_githubactions()

    assert object.public_key_id is None
    assert object.public_key is None

    response = object.get_repo_public_key()
    patched_requests.assert_called_with(REPO_PUBLIC_KEY_URL, headers=AUTH_HEADERS)

    assert response_data == response

    assert object.public_key_id is not None
    assert object.public_key is not None
    assert object.public_key_id == response_data.get("key_id")
    assert object.public_key == response_data.get("key")


@patch("requests.get")
def test_get_repo_public_key_fail(patched_requests, get_githubactions):
    """Test if `get_repo_public_key` raises exception."""
    patched_requests.return_value.status_code = 400
    with pytest.raises(Exception):
        get_githubactions().get_repo_public_key()


# @pytest.mark.asyncio
# @patch("secrets_updater.utility.encrypt")
# @patch("secrets_updater.github.GitHubActions.get_repo_public_key")
# @patch("aiohttp.ClientSession.put")
# async def test_create_or_update_repo_secret_success(patched_client,
#                                               patched_get_repo_public_key,
#                                               patched_encrypt,
#                                               get_githubactions):
#     """Test if `create_or_update_repo_secret` returns valid data."""
#     secret_name = "super secrete name"
#     secret_value = "super secrete value"
#
#     object = get_githubactions()
#
#     object.create_or_update_repo_secret(secret_name, secret_value)
#
#     # await patched_client.assert_called()
#     await patched_get_repo_public_key.assert_called()
#     await patched_encrypt.assert_called()
