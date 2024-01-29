"""Test cases for wrapper `main`."""

# Standard Library
import os

from unittest.mock import AsyncMock, call, patch

# 3rd Party Libraries
import pytest

# Project Libraries
from secrets_updater.main import add_local_env_to_secrets, add_secretes
from secrets_updater.settings import ENV_FILE_PATH


pytest_plugin = ("pytest_asyncio",)


@pytest.mark.asyncio
@patch("github.encrypt")
@patch("aiohttp.ClientSession.put")
@patch("secrets_updater.github.requests.get")
async def test_add_local_env_to_secrets(
    patched_request,
    patched_client,
    patched_encrypt,
    get_githubactions,
    secrete_file_content,
    get_secretes_file,
    get_public_key_details,
):
    """Test if `add_local_env_to_secrets` runs as intended."""
    patched_request.return_value.status_code = 200
    patched_request.return_value.json.return_value = get_public_key_details

    patched_client.return_value.status.return_value = 204
    patched_encrypt.return_value = "encrypted secrete value using public key"

    await add_local_env_to_secrets("fakefile")

    assert patched_client.call_count == 2


@patch("secrets_updater.main.add_local_env_to_secrets")
@patch("os.listdir")
@patch("os.path.exists")
def test_add_secretes(patched_path_exists, patched_listdir, patched_function):
    """Test if `add_secretes` runs as intended."""
    patched_listdir.return_value = [
        ".sample-env-file-1",
        ".sample-env-file-2",
        ".sample-env-file-3",
    ]
    patched_path_exists.return_value = True
    patched_function.return_value = AsyncMock()

    add_secretes()

    calls = [call(os.path.join(ENV_FILE_PATH, _)) for _ in patched_listdir.return_value]

    assert patched_function.await_count == 3
    assert patched_function.await_args_list == calls
