.. IMPORTANT::
   The plugins support in pysteps is only available for versions >=1.4.

Cookiecutter Pysteps-plugin
===========================

.. README_BEGIN_TAG

Cookiecutter template for Pysteps plugins.
Cookiecutter_ is a command-line utility to creates python packages projects from
templates, called "cookiecutters."

.. _Cookiecutter: https://cookiecutter.readthedocs.io

.. note:: **Important**: Currently, only importers are supported as plugins.

.. _how_plugins_work:

How do the plugins work?
========================

When the plugin is installed, it advertises the new importers to other packages
(in our case, pysteps) using the python `entry points specification`_.
These new importers are automatically discovered every time that the pysteps library is
imported. The discovered importers are added as attributes to the io.importers module
and registered to the io.get_method interface without any user intervention.
In addition, since the plugins' installation does not modify the actual pysteps
installation (i.e., the pysteps sources), the pysteps library can be updated without
reinstalling the plugin.

.. _`entry points specification`: https://packaging.python.org/specifications/entry-points/

Quickstart
----------

Install the latest Cookiecutter::

    pip install -U cookiecutter

To generate a skeleton for a Pysteps plugin in the current folder, simply run::

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

.. README_END_TAG

.. CREDITS_BEGIN_TAG

Credits
-------

The cookiecutter-pysteps-plugin template was adapted from the cookiecutter-pypackage_
template.

.. _cookiecutter-pypackage: https://github.com/audreyfeldroy/cookiecutter-pypackage

.. CREDITS_END_TAG