.. IMPORTANT::
   The Plugin support for Pysteps is an experimental feature that is is not supported
   by any stable release or the main branch in the Pysteps repository.
   This repository is being used mostly for testing purposes.

===========================
Cookiecutter Pysteps-plugin
===========================

Cookiecutter template for Pysteps plugins packages. Currently, **only importers** are
supported as plugins.

**Cookiecutter** is a command-line utility to creates python packages projects from
templates, called "cookiecutters".

Quickstart
----------

Install the latest Cookiecutter::

    pip install -U cookiecutter

Generate a Pysteps plugin package project using::

    cookiecutter https://github.com/aperezhortal/cookiecutter-pysteps-plugin

When the above command is run, you are ask to enter the following values that appears in
different parts of your generated project:

- **full_name**: Your full name.
- **email**: Your email address.
- **project_name**: The name of your new Pysteps plugin.
- **project_slug**: The namespace of your Python package. This should be Python import-friendly.
  That is, no spaces, no hyphens, and no special characters.
- **project_short_description**: A short description the Pysteps plugin.
- **importer_name**: Name of the module implementing the importers.
- **version**: The starting version number for your project.
- **open_source_license**. Choose a license for your project.
  Options: [1. MIT License, 2. BSD license, 3. ISC license, 4. Apache Software License 2.0, 5. GNU General Public License v3, 6. Not open source]


Credits
-------

The cookiecutter-pysteps-plugin template is mostly based on the cookiecutter-pypackage_
template.

.. _cookiecutter-pypackage: https://github.com/audreyfeldroy/cookiecutter-pypackage

