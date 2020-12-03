.. _tutorial:

===============================
Create your own importer plugin
===============================

Since version 1.4, pysteps allows the users to add new importers by installing external
packages, called plugins, without modifying the pysteps installation. These plugins need
to follow a particular structure (described next) to allow pysteps to discover and
integrate the new importers to the pysteps interface without any user intervention.

.. contents:: Table of Contents
    :local:
    :depth: 3

How do the plugins work?
===================

When the plugin is installed, it advertises the new importers to other packages
(in our case, pysteps) using the python `entry points specification`_.
These new importers are automatically discovered every time that the pysteps library is
imported. The discovered importers are added as attributes to the io.importers module
and registered to the io.get_method interface without any user intervention.
In addition, since the plugins' installation does not modify the actual pysteps
installation (i.e., the pysteps sources), the pysteps library can be updated without
reinstalling the plugin.

.. _`entry points specification`: https://packaging.python.org/specifications/entry-points/


Create your plugin using this cookiecutter template
=====================================

The easier way to create a pysteps plugin is using the **cookiecutter-pysteps-plugin**
template that quickly builds a skeleton for the new plugin python package.

First, install the latest Cookiecutter if it is not available::

    pip install -U cookiecutter

Once Cookiecutter_ is installed, to create the skeleton for the plugin package, run::

    cookiecutter https://github.com/pysteps/cookiecutter-pysteps-plugin

The above command will prompt the user to enter the following values used to generate
a skeleton for the plugin package:

- **full_name**: Your full name.
- **email**: Your email address.
- **project_name**: The name of your new Pysteps plugin.
- **project_slug**: The namespace of your Python package.
  The name should be Python import friendly (no spaces, no hyphens, and no special
  characters).
- **project_short_description**: Short description of the plugin.
- **importer_name**: Name of the module implementing the importers.
- **version**: The starting version number for your project.
- **open_source_license**. Choose a license for your project.
  Options: [1. MIT License, 2. BSD license, 3. ISC license, 4. Apache Software License
  2.0, 5. GNU General Public License v3, 6. Not open source]

IMPORTANT: In the rest of the tutorial, we will refer to the values entered by the user
as <variable>. For example, <full_name> denotes the value entered by the user when
**full_name** is prompted.

.. _Cookiecutter: https://cookiecutter.readthedocs.io

The previous command creates a package skeleton name <project_name> in the current
folder.

Plugin project structure
------------------------

The plugin template skeleton has the following default structure:

::

    <project_name>
    ├── docs
    │   ├── conf.py
    │   ├── index.rst
    │   ├── installation.rst
    │   ├── make.bat
    │   ├── Makefile
    │   ├── readme.rst
    │   └── requirements.txt
    ├── LICENSE  (*a copy of the selected license*)
    ├── MANIFEST.in
    ├── <project_slug>
    │   ├── <importer_name>.py
    │   └── __init__.py
    ├── README.rst
    ├── requirements_dev.txt
    ├── setup.cfg
    ├── setup.py
    ├── tests
    │   ├── __init__.py
    │   └── test_pysteps_<importer_name>.py
    └── tox.ini


Project name (<project_name>)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the project name, it is recommended using the following convention:
**pysteps-importer-<institution short name>**.
Note that this convention is not strictly needed, and any name can be used.


Package name (<project slug>)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    <project_name>
    └── <project_slug>

This is the name of our package containing the new importers for pysteps. The package
name should not contain spaces, hyphens, or uppercase letters. The same naming
convention as the package name is recommended. Note that the package name should be
Python import friendly (no spaces, no hyphens, and no special characters).


Importer module (<importer_name>)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    <project_name>
    └── <project_slug>pysteps-importer-abc
            ├── <importer_name>.py
            └── __init__.py

Name of the module implementing the new importers.
The module's name must start with "importer_" prefix. This is strictly needed for the
pysteps interface to work correctly.

README
~~~~~~

::

    <project_name>
    └── README.rst

Project readme with a brief description of the plugin.

IMPORTANT: The readme file provided by default is very general. Modify its contents to
describe your package better.


setup.py and setup.cfg
~~~~~~~~~~~~~~~~~~~~~~

::

    <project_name>
    ├── requirements_dev.txt
    ├── setup.cfg
    └── setup.py

`setup.py`` is the build script used for setuptools to install and build the package.
These files contain the information about your package (like name, author, version,
dependencies, etc.) and which code files to include. For more information on `setup.py`
see https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py

The `setup.cfg` file contains the default configuration used to build and install the
script. This file is optional.

The `requirements_dev.txt` file contains a list of the packages required by the plugin.

Manifest.in
~~~~~~~~~~~

::

    <project_name>
    └── MANIFEST.in

If you don't supply an explicit list of files, the installation using `setup.py` will
include only the minimal files needed for the package to run (e.g., the \*.py files)

The Manifest.in file contains the list of additional files and directories to be
included in your source distribution. For more information about the manifest file, see
https://packaging.python.org/guides/using-manifest-in/

Documentation
~~~~~~~~~~~~~

::

    <project_name>
    └── docs
    │   ├── conf.py
    │   ├── index.rst
    │   ├── installation.rst
    │   ├── make.bat
    │   ├── Makefile
    │   ├── readme.rst
    │   └── requirements.txt
    └── tox.ini (optional)

By default, the plugin template includes a skeleton for the package documentation to
be build using sphinx. This is not strictly needed, although it is highly recommended
if the package is released as an open-source package.

Also, a simple configuration file for tox_ is included
in the template to build the documentation quickly. If tox is installed, the
documentation can be build by executing the `tox` command from the project root.
The command will print the path where the
documentation is built.

.. _tox: https://tox.readthedocs.io/en/latest/

A short description of the files included in the skeleton is presented next:

index.rst:
    This is the index file for the documentation.

readme.rst (optional):
    This file can be used to include the content of the package README.

installation.rst (optional)
    Instruction to install the plugin.

conf.py:
    Sphinx configuration. A good set of default parameters are provided by default.

Makefile & make.bat:
    Interface for local development used by sphinx. Modify only if needed.

requirements.txt:
    List of dependencies used to build the documentation (python packages).

A detailed explanation of how to write the package documentation using sphinx is outside
this tutorial's scope.
For additional information, the following tutorials are recommended:

https://sphinx-tutorial.readthedocs.io/start/

https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html

https://pythonhosted.org/an_example_pypi_project/sphinx.html


Tests
~~~~~

::

    <project_name>
    └── tests
    │    ├── __init__.py
    │    └── test_pysteps_<importer_name>.py
    └── tox.ini (optional)


The template includes a minimum number of tests (using pysteps) that check that plugin
can be installed properly and be detected by pysteps.

A simple configuration file for tox_ is included in the template to run the tests
quickly. If tox is installed, the tests suite is run executing the `tox` command from the project root.

.. _tox: https://tox.readthedocs.io/en/latest/
