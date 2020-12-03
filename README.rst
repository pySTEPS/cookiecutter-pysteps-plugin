.. IMPORTANT::
   The plugins support in pysteps is only available for versions >=1.4.

===========================
Cookiecutter Pysteps-plugin
===========================

Cookiecutter template for Pysteps plugins.
**Important**:  Currently, only importers can be added to pysteps using plugins.

**Cookiecutter** is a command-line utility to creates python packages projects from
templates, called "cookiecutters."

Quickstart
----------

Install the latest Cookiecutter::

    pip install -U cookiecutter

Generate a Pysteps plugin package project using::

    cookiecutter https://github.com/pysteps/cookiecutter-pysteps-plugin

The above command will prompt the user to enter the following values used to generate
a skeleton for the plugin package:

- **full_name**: Your full name.
- **email**: Your email address.
- **project_name**: The name of your new Pysteps plugin.
- **project_slug**: The namespace of your Python package.
  The name should be Python import friendly (no spaces, no hyphens, and no
  special characters).
- **project_short_description**: Short description of the plugin.
- **importer_name**: Name of the module implementing the importers.
- **version**: The starting version number for your project.
- **open_source_license**. Choose a license for your project.
  Options: [1. MIT License, 2. BSD license, 3. ISC license, 4. Apache Software License
  2.0, 5. GNU General Public License v3, 6. Not open source]


Credits
-------

The cookiecutter-pysteps-plugin template was adapted from the cookiecutter-pypackage_
template.

.. _cookiecutter-pypackage: https://github.com/audreyfeldroy/cookiecutter-pypackage
