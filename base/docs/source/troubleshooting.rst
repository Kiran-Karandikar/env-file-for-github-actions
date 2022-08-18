.. Trouble shooting readme.

Troubleshooting
=====================================

This page contains some advice about errors and problems commonly encountered during the development.

Docker:
-------

To fix unknown docker related issues, you can either:

- Clear your project-related Docker cache with ``docker compose -f local.yml down --volumes --rmi all``.
- Use the Docker volume sub-commands to find volumes (`ls`_) and remove them (`rm`_).
- Use the `prune`_ command to clear system-wide (use with care!).

.. _ls: https://docs.docker.com/engine/reference/commandline/volume_ls/
.. _rm: https://docs.docker.com/engine/reference/commandline/volume_rm/
.. _prune: https://docs.docker.com/v17.09/engine/reference/commandline/system_prune/

Others
------

..

    Permission denied while executing bash script in GitHub Actions.

That most likely means that your <path_to_script>/<script_name>.sh script doesn't have the execute filesystem permission set.

Instruct git to add the permission anyway with this command:

.. code-block::

    $ git update-index --chmod=+x <path_to_script>/<script_name>.sh
    $ git commit -m "Changing file permissions"

update-index is similar to add in that it adds the change to the index, so you have to commit and push as usual.
