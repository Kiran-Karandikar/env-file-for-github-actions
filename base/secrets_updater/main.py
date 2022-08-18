"""Wrapper Script to invoke GitHub api and related operations.

See Also:
    1. https://docs.python.org/3/library/asyncio-policy.html?highlight=set_event_loop_policy#asyncio.WindowsSelectorEventLoopPolicy  # noqa: E501
"""
# Standard Library
import asyncio
import os
import sys


sys.path.insert(0, os.path.abspath(".."))

# Project Libraries
from secrets_updater.github import GitHubActions  # noqa: E402
from secrets_updater.settings import (  # noqa: E402
    ENV_FILE_PATH,
    EXCLUDE_ENV_FILES_FROM_UPLOAD,
)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def add_local_env_to_secrets(env_file_path):
    """Upload secrets defined in ``env_file_path`` to GitHub actions.

    Every secret listed in ``env_file_path`` will be updated to repository
    secrets.Except Secrets starting with ``#``

    Args:
        env_file_path (str): Complete file path of local environment file.

    See Also:
        1. https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task
    """
    github_object = GitHubActions()
    background_tasks = set()

    with open(env_file_path) as fp:
        for line in fp:
            if line.startswith("#") or not line.strip():
                continue
            key, value = line.strip().split("=", 1)
            print(f"Adding :{key} to Github Actions Secret.")
            task = asyncio.create_task(
                github_object.create_or_update_repo_secret(key, value)
            )
            # Add task to the set. This creates a strong reference.
            background_tasks.add(task)
            # To prevent keeping references to finished tasks forever,
            # make each task remove its own reference from the set after
            # completion:
            task.add_done_callback(background_tasks.discard)
        await asyncio.gather(*background_tasks)


def add_secretes():
    """Invokes async upload action for every env file defined in ``ENV_FILE_PATH``.

    All env files defined in ``EXCLUDE_ENV_FILES_FROM_UPLOAD`` will be excluded from
    upload.
    """
    for env_file in filter(
        lambda x: x not in EXCLUDE_ENV_FILES_FROM_UPLOAD, os.listdir(ENV_FILE_PATH)
    ):
        file_path = os.path.join(ENV_FILE_PATH, env_file)
        if os.path.exists(file_path):
            asyncio.run(add_local_env_to_secrets(file_path))


if __name__ == "__main__":
    add_secretes()
