"""
# Docstring.
"""
# Standard Library
import json

# 3rd Party Libraries
import aiohttp
import requests

from settings import AUTH_HEADERS, REPO_PUBLIC_KEY_URL, SECRETS_URL
from utility import encrypt


class GitHubActions:
    """ """

    def __init__(self):
        self.public_key_id = None
        self.public_key = None

    def get_repo_secrets(self, *args, **kwargs):
        """

        Args:
            *args:
            **kwargs:

        Returns:

        See Also:
            1. https://docs.github.com/en/rest/actions/secrets#list-repository-secrets
            2. https://docs.github.com/en/rest/actions/secrets#list-environment-secrets
        """
        response = requests.get(SECRETS_URL, headers=AUTH_HEADERS)
        if response.status_code != 200:
            raise Exception("Something Went wrong...")
        return response.json()

    def get_repo_public_key(self, *args, **kwargs):
        response = requests.get(REPO_PUBLIC_KEY_URL, headers=AUTH_HEADERS)
        if response.status_code != 200:
            raise Exception("Something Went wrong...")
        data = response.json()
        self.public_key = data.get("key")
        self.public_key_id = data.get("key_id")
        return data

    async def create_or_update_repo_secret(self, secret_name, secret_value):
        """

        Args:
            secret_name:
            secret_value:

        Returns:

        See Also:
            1. https://docs.github.com/en/rest/actions/secrets#create-or-update-a-repository-secret
        """
        if self.public_key_id is None or self.public_key is None:
            self.get_repo_public_key()

        encrypted_secret = encrypt(self.public_key, secret_value)

        data = {"encrypted_value": encrypted_secret, "key_id": self.public_key_id}
        request_url = f"{SECRETS_URL}/{secret_name}"
        # response = requests.put(request_url, headers=AUTH_HEADERS, data=json.dumps(data))
        # if response.status_code != 201:
        #     raise Exception("Something Went wrong...")
        async with aiohttp.ClientSession() as session:
            async with session.put(
                request_url, headers=AUTH_HEADERS, data=json.dumps(data)
            ) as response:
                if response.status == 204:
                    print(f"Secret: {secret_name} already exists !!!")
                else:
                    print(f"Secret: {secret_name} Added !!!")
