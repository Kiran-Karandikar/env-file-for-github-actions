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

That most likely means that your ./.github/scripts/backend_decrypt.sh script doesn’t have the “execute” filesystem permission set. I assume you’re developing on Windows locally, which doesn’t have that kind of permission system.

You can tell git to add the permission anyway with this command:

git update-index --chmod=+x provisioning/import_provisioning.sh
git commit -m "Changing file permissions"

update-index is similar to add in that it adds the change to the index, so you’ll have to commit and push as usual.
