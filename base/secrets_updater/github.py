"""Methods/Classes to interact with GitHub API.

Supports fetching `repo_secrets`, `repo_public_key` and creation or update of
**`repo_secret`**
"""
# Standard Library
import json

# 3rd Party Libraries
import aiohttp
import requests

# Project Libraries
from settings import AUTH_HEADERS, REPO_PUBLIC_KEY_URL, SECRETS_URL
from utility import encrypt


class GitHubActions:
    """Provides methods to interact with GitHub API."""

    def __init__(self):
        self.public_key_id = None
        self.public_key = None

    def get_repo_secrets(self, *args, **kwargs):
        """Get repo secrets. Uses `list-repository-secrets` endpoint.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: Json Response.

        Raises:
            `Exception`: if response status code is other than 200.

        See Also:
            1. https://docs.github.com/en/rest/actions/secrets#list-repository-secrets
            2. https://docs.github.com/en/rest/actions/secrets#list-environment-secrets
        """
        response = requests.get(SECRETS_URL, headers=AUTH_HEADERS)
        if response.status_code != 200:
            raise Exception("Something Went wrong...")
        return response.json()

    def get_repo_public_key(self, *args, **kwargs):
        """Get repo public key. Uses `get-a-repository-public-key` endpoint.

        Public key is required to encrypt secrets while creating or updating secrets
        for particular repo.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: Containing Public key details. `key` and `key_id`.

        Raises:
             `Exception`: if response status code is other than 200.

        See Also:
            1. https://docs.github.com/en/rest/actions/secrets#get-a-repository-public-key
        """
        response = requests.get(REPO_PUBLIC_KEY_URL, headers=AUTH_HEADERS)
        if response.status_code != 200:
            raise Exception("Something Went wrong...")
        data = response.json()
        self.public_key = data.get("key")
        self.public_key_id = data.get("key_id")
        return data

    async def create_or_update_repo_secret(self, secret_name, secret_value):
        """Create repository secret, update if already exists. Uses `create-or-update-a-repository-secret` endpoint.

        Public key is required to encrypt secrets while creating or updating
        secrets for particular repo.

        Args:
            secret_name (str): Name of secrete.
            secret_value (utf-8): Secrete value encrypted using public key.

        Returns:
            None

        See Also:
            1. https://docs.github.com/en/rest/actions/secrets#create-or-update-a-repository-secret
            2. https://docs.aiohttp.org/en/stable/client_reference.html
        """
        if self.public_key_id is None or self.public_key is None:
            self.get_repo_public_key()

        encrypted_secret = encrypt(self.public_key, secret_value)

        data = {"encrypted_value": encrypted_secret, "key_id": self.public_key_id}
        request_url = f"{SECRETS_URL}/{secret_name}"

        async with aiohttp.ClientSession() as session:
            async with session.put(
                request_url, headers=AUTH_HEADERS, data=json.dumps(data)
            ) as response:
                if response.status == 204:
                    print(f"Secret: {secret_name} already exists !!!")
                else:
                    print(f"Secret: {secret_name} Added !!!")
