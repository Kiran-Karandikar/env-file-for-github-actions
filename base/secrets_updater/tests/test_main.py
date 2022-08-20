# """Test cases for wrapper `main`."""
# # Standard Library
# from unittest.mock import patch
#
# # 3rd Party Libraries
# import pytest
#
# # Project Libraries
# from secrets_updater.main import add_local_env_to_secrets, add_secretes
#
#
# pytest_plugin = ("pytest_asyncio",)
#
#
# @pytest.mark.asyncio
# @patch("secrets_updater.utility.encrypt")
# @patch("aiohttp.ClientSession.put")
# @patch("secrets_updater.github.requests.get")
# async def test_add_local_env_to_secrets(
#     patched_request,
#     patched_client,
#     patched_encrypt,
#     get_githubactions,
#     secrete_file_content,
#     get_secretes_file,
#     get_public_key_details,
# ):
#     """Test if `add_local_env_to_secrets` runs as intended."""
#     patched_request.return_value.status_code = 200
#     patched_request.return_value.json.return_value = get_public_key_details
#
#     patched_client.return_value.status.return_value = 204
#     patched_encrypt.return_value = "encrypted secrete value using public key"
#
#     await add_local_env_to_secrets("fakefile")
#
#     assert patched_client.call_count == 2
#
#
# @pytest.mark.asyncio
# @patch("secrets_updater.main.add_local_env_to_secrets")
# @patch("main.os")
# async def test_add_secretes(patched_os, patched_function):
#     """Test if `add_secretes` runs as intended."""
#     patched_os.listdir.return_value = [
#         ".sample-env-file-1",
#         ".sample-env-file-2",
#         ".sample-env-file-3",
#     ]
#     patched_os.path.exists.return_value = True
#
#     await add_secretes()
#
#     assert patched_function.call_count == 3
