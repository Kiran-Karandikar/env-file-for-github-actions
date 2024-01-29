"""Initialize environment variables."""

# Standard Library
import os

# 3rd Party Libraries
import environ


env = environ.Env()

# Set the project base directory
LOCAL_ENV = ".envs/.local"
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENV_FILE_PATH = os.path.join(BASE_DIR, LOCAL_ENV)
EXCLUDE_ENV_FILES_FROM_UPLOAD = [".gh_credentials"]

# Take environment variables from .env file
# For non-docker based
environ.Env.read_env(env_file=os.path.join(ENV_FILE_PATH, ".gh_credentials"))
# ------------------------------------------------------------------------------
# Github Credentials
# ------------------------------------------------------------------------------
TOKEN = env("GH_ACCESS_TOKEN", default="!!!! CREATE PERSONAL ACCESS TOKEN!!!")
OWNER = env("OWNER", default="kiran-karandikar")
REPO = env("REPO", default="env-file-for-github-actions")

AUTH_HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {TOKEN}",
}

SECRETS_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/secrets"
REPO_PUBLIC_KEY_URL = f"{SECRETS_URL}/public-key"
