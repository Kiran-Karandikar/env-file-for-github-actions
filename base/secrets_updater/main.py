# Standard Library
import asyncio
import os
import sys

# 3rd Party Libraries
from github import GitHubActions
from settings import BASE_DIR


# https://docs.python.org/3/library/asyncio-policy.html?highlight=set_event_loop_policy#asyncio.WindowsSelectorEventLoopPolicy  # noqa: E501
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def add_local_env_to_secrets(env_file_path):
    """
    # todo
    Args:
        env_file_path:

    Returns:

    See Also:
        1. https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task
    """
    github_object = GitHubActions()
    github_object.get_repo_public_key()
    background_tasks = set()

    with open(env_file_path) as fp:
        for line in fp:
            if line.startswith("#") or not line.strip():
                continue
            key, value = line.strip().split("=", 1)
            print(f"Adding :{key} to Github Actions Secret.")
            # asyncio.run(github_object.create_or_update_repo_secret(key, value))
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
    """
    # Todo
    Returns:

    """
    env_files_path = os.path.join(BASE_DIR, ".envs/.local")
    env_files = os.listdir(env_files_path)
    exclude_files = [".gh_credentials"]
    for env_file in filter(lambda x: x not in exclude_files, env_files):
        file_path = os.path.join(env_files_path, env_file)
        if os.path.exists(file_path):
            asyncio.run(add_local_env_to_secrets(file_path))


if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath("../.."))
    add_secretes()
