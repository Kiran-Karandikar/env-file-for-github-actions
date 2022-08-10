import json

import requests
from pprint import pprint
from base64 import b64encode
from nacl import encoding, public

# https://docs.github.com/en/rest/actions/secrets#list-repository-secrets
# https://docs.github.com/en/rest/actions/secrets#list-environment-secrets
# github username

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f'token {token}',
}
# r = requests.post(url, headers=self.headers)
# url to request
url = f"https://api.github.com/repos/{owner}/{repo}/actions/secrets"
# make the request and return the json
user_data = requests.get(url, headers=headers).json()
# pretty print JSON data
pprint(user_data)
for secret_dict in user_data.get("secrets"):
    print(secret_dict.get("name"))


# Put secret
# https://docs.github.com/en/rest/actions/secrets#create-or-update-a-repository-secret


def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a Unicode string using the public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")


url = f"https://api.github.com/repos/{owner}/{repo}/actions/secrets/public-key"
# make the request and return the json
user_data = requests.get(url, headers=headers).json()
pprint(user_data)


secret_name = "some_other_secret_value"
secret_value = "My Name is Kiran"
encrypted_secret = encrypt(user_data.get("key"), secret_value)
pprint(encrypted_secret)
url = f"https://api.github.com/repos/{owner}/{repo}/actions/secrets/{secret_name}"

data = {"encrypted_value": encrypted_secret, "key_id": user_data.get("key_id")}
user_data = requests.put(url, headers=headers, data=json.dumps(data)).json()
pprint(user_data)

# -------------------------------------------------------------------------------------
# repo = 'some_repo'
# description = 'Created with api'
#
# payload = {'name': repo, 'description': description, 'auto_init': 'true'}
#
# login = requests.post('https://api.github.com/' + 'user/repos', auth=(user, token),
#                       data=json.dumps(payload)
#                       )
# user = 'username'
# headers = {'Authorization': 'token ' + token}
#
# login = requests.delete('https://api.github.com/' + 'repos/' + user + '/' + repo,
#                         headers=headers
#                         )

# headers = {'Authorization': 'token ' + token}
#
# login = requests.get('https://api.github.com/user', headers=headers)
# print(login.json())

# username = 'user'
# token = 'token'
#
# login = requests.get('https://api.github.com/search/repositories?q=github+api',
#                      auth=(username, token)
#                      )



# r = requests.post(
#     url=url,
#     data=json_data,
#     headers=headers
# )
