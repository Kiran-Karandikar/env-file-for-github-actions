.. _workflow:

Workflow
=========

.. index:: Workflow

.. seealso::

    :ref:`environ` for environment configuration.
    :ref:`with_docker` for guide on docker setup.

- Create the required environment files under ``LOCAL_ENV``.
- Update ``ci.yml`` to export these variables dynamically. Below is example.

    .. code-block::

        mkdir -p .envs/.local
        touch .envs/.local/.sample
        echo SECRET_1=${{ secrets.SECRET_1 }} >> .envs/.local/.sample
        echo SECRET_2=${{ secrets.SECRET_2 }} >> .envs/.local/.sample

    .. note::

        For every file under ``LOCAL_ENV``. Add those secrets to respective files.
        Using multiple echo commands for each and every env file.

        .. code-block::

            touch .envs/.local/.sample_file_1
            echo SECRET_1=${{ secrets.SECRET_1 }} >> .envs/.local/.sample_file_1
            touch .envs/.local/.sample_file_2
            echo SECRET_4=${{ secrets.SECRET_4 }} >> .envs/.local/.sample_file_2

- Update the env file location in ``local.yml``.
- To add the secrets defined under ``LOCAL_ENV`` to github actions either use ``pre-commit`` hook or upload manually.

Using Pre-commit Hook
---------------------

- `pre-commit`_ should be installed on your local machine, and then::

    $ pre-commit install
    $ pre-commit install --hook-type pre-push

- The ``pre-commit`` ``pre-push`` hook uploads the secrete to github actions when **ONLY** ``push`` operation is performed.
- Under hood it runs ``python base/secrets_updater/main.py``

Uploading Manually
------------------

- Run ``python base/secrets_updater/main.py`` which will automatically upload all secrets.

.. note::

    All secretes will be either created or overridden as per GitHub API. Update action make take a while based upon the total number of environment secrets.


.. _`pre-commit`: https://pre-commit.com/#install
