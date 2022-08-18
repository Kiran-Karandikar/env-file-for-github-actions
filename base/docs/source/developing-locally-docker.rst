.. _with_docker:

Getting Up and Running Locally With Docker
==========================================

.. index:: Docker

The steps below will get you up and running with a local development environment.
All of these commands assume you are in the root of your generated project.

.. note::

    If you're new to Docker, please be aware that some resources are cached system-wide
    and might reappear if you generate a project multiple times with the same name.

.. seealso::

   Check out the :ref:`environ` page for a environments details.

Prerequisites
-------------

* Docker; if you don't have it yet, follow the `installation instructions`_;
* Docker Compose; refer to the official documentation for the `installation guide`_.
* Pre-commit; refer to the official documentation for the `pre-commit`_.

.. _`installation instructions`: https://docs.docker.com/install/#supported-platforms
.. _`installation guide`: https://docs.docker.com/compose/install/
.. _`pre-commit`: https://pre-commit.com/#install

Build the Stack
---------------

This can take a while, especially the first time you run this particular command on your development system::

    $ docker-compose -f local.yml build

Generally, if you want to emulate production environment use ``production.yml`` instead. And this is true for any other actions you might need to perform: whenever a switch is required, just do it!

Before doing any git commit, `pre-commit`_ should be installed globally on your local machine, and then::

    $ git init
    $ pre-commit install
    $ pre-commit install --hook-type pre-push

Failing to do so will result with a bunch of CI and Linter errors that can be avoided with pre-commit.


Run the Stack
-------------

Open a terminal at the project root and run the following for local development::

    $ docker compose -f local.yml up

You can also set the environment variable ``COMPOSE_FILE`` pointing to ``local.yml`` like this::

    $ export COMPOSE_FILE=local.yml

And then run::

    $ docker-compose up

To run in a detached (background) mode, just::

    $ docker-compose up -d


Get into docker container's shell.: ::

    $ docker ps
    $ docker exec -it <container_name> bash

.. _envs:

Configuring the Environment
---------------------------

This is the excerpt from your project's ``local.yml``: ::

  # ...

  sample-container:
    env_file:
      - ./base/.envs/.local/.sample-env-file-name

  # ...

The most important thing for us here now is ``env_file`` section enlisting ``./base/.envs/.local/.sample-env-file-name``. Generally, the stack's behavior is governed by a number of environment variables (`env(s)`, for short) residing in ``envs/``: ::

    .envs
    ├── .local
        └── .sample-env-file-name
    └── .production
        └── .sample-env-file-name

By convention, for any service ``sI`` in environment ``e`` (you know ``someenv`` is an environment when there is a ``someenv.yml`` file in the project root), given ``sI`` requires configuration, a ``.envs/.e/.sI`` ``service configuration`` file exists.

Consider the aforementioned ``./base/.envs/.local/.sample-env-file-name``: ::

    SECRET_1=Some random value 1
    SECRET_2=Some random value 2

Tips & Tricks
-------------

Activate a Docker Machine
~~~~~~~~~~~~~~~~~~~~~~~~~

This tells our computer that all future commands are specifically for the dev1 machine. Using the ``eval`` command we can switch machines as needed.::

    $ eval "$(docker-machine env dev1)"

Debugging
~~~~~~~~~

ipdb
"""""

If you are using the following within your code to debug: ::

    import ipdb;
    ipdb.set_trace()

Then you may need to run the following for it to work as desired: ::

    $ docker-compose -f local.yml run --rm --service-ports <container_name>

docker
""""""

The ``container_name`` from the yml file can be used to check on containers with docker commands, for example: ::

    $ docker logs sample_container
    $ docker top docs
