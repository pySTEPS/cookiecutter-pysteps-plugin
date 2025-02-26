.. IMPORTANT::
   The plugins support in pysteps is only available for versions >=1.4.

Cookiecutter Pysteps-plugin
===========================

.. README_BEGIN_TAG

Cookiecutter template for Pysteps plugins.
Cookiecutter_ is a command-line utility to creates python packages projects from
templates, called "cookiecutters."

.. _Cookiecutter: https://cookiecutter.readthedocs.io

.. note:: **Important**: Currently, only importers and postprocessors are supported as plugins.

.. _how_plugins_work:

How do the plugins work?
========================

When the plugin is installed, it advertises the new functions to other packages
(in our case, pysteps) using the python `entry points specification`_.
These new functions are automatically discovered every time that the pysteps library is
imported. The discovered functions are added as attributes to their specified module
and registered to the module's interface without any user intervention. For example, in the case of an importer plugin, the importers would be added as attributes to the io.importers module and registered to the io.get_method interface.
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
- **plugin_type**: The type of plugin you would like to create.
  Options: [1. importer, 2. diagnostic]
- **plugin_subtype**: Any string is allowed. The importer type can use the institution as as subtype, while an empty string is the default for a diagnostic.
- **project_name**: The repository name. This is also the name of the plugin root directory used to install the Python package. Recommended: *pysteps-[plugin_type][-plugin_subtype]-[name]* where *name* is the main functionality.
- **project_slug**: The namespace of your Python package. The slug should be Python import friendly (no spaces, no hyphens, and no special characters).
- **plugin_name**: Name of the module implementing the plugin. Importer modules should start with *importer_*. Diagnostic modules should start with *diagnostic_*.
- **plugin_function**: Name of the function that is set as primary pysteps entry point for the plugin. Importer functions should start with *import_*. Diagnostic functions should start with *diagnostic_*.
- **project_short_description**: Short description of the plugin.
- **version**: The starting version number for your project.
- **open_source_license**. Choose a license for your project.
  Options: [1. MIT License, 2. BSD license, 3. ISC license, 4. Apache Software License
  2.0, 5. GNU General Public License v3, 6. Not open source]

This creates a local directory ``[project_name]`` as the template for your plugin.

- modify the function ``[plugin_function]`` in ``[project_name]/[project_slug]/[plugin_type]/[plugin_name].py`` to your needs
- if you add more functions in ``[project_name]/[project_slug]/[plugin_type]/[plugin_name].py`` make sure to create the additional entry points in ``[project_name]/setup.py``

.. README_END_TAG

.. CREDITS_BEGIN_TAG

Credits
-------

The cookiecutter-pysteps-plugin template was adapted from the cookiecutter-pypackage_
template.

.. _cookiecutter-pypackage: https://github.com/audreyfeldroy/cookiecutter-pypackage

.. CREDITS_END_TAG
