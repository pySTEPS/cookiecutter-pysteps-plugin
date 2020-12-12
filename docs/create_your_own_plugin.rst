.. _create_your_own_plugin:

===============================
Create your own importer plugin
===============================

Since version 1.4, pysteps allows the users to add new importers by installing external
packages, called plugins, without modifying the pysteps installation. These plugins need
to follow a particular structure (described next) to allow pysteps to discover and
integrate the new importers to the pysteps interface without any user intervention.
For a short description of how the plugins work, see :ref:`how_plugins_work`.
There are two ways of creating your plugin. The first one involves building the plugin
from scratch. An easier alternative is using a Cookiecutter template that easily builds
the skeleton for the new importer plugin.

There are two ways of creating a plugin. The first one is building the importers plugin
from scratch. However, an easier alternative is using this `Cookiecutter`_ template
to create the skeleton for the new importer plugin, and then customize it.
However, this can be a daunting task if you are creating your first plugin.
Hence, before customizing the cookiecutter template, let's review the main components of
the plugin architecture by describing how to build an importers plugin from scratch.

After you are familiar with the plugin fundamentals, you can build your plugin from the
cookiecutter template. For a detailed description of the template, see
:ref:`plugin_template_description`.

.. _Cookiecutter: https://cookiecutter.readthedocs.io

Minimal plugin project
----------------------

Let's suppose that we want to add two new importers to pysteps for reading the radar
composites from the "Awesome Bureau of Composites", kindly abbreviated as "abc".
The composites provided by this institution are available in two different
formats: Netcdf and Grib2. The details of each format are not important for the rest of
this description. Just remember the names of the two formats.

Without further ado, let's create a python package  (a.k.a. the plugin) implementing the
two importers. For simplicity, we will only include the elements that are strictly
needed for the plugin to be installed and to work correctly.

The minimal python package to implement an importer plugin has the following
structure:

::

    pysteps-importer-abc        (project name)
    ├── pysteps_importer_abc    (package name)
    │  ├── importer_abc_xyz.py  (importer module)
    │  └── __init__.py          (Initialize the pysteps_importer_abc package)
    ├── setup.py                (Build and installation script)
    └── MANIFEST.in             (manifest template)

Project name
~~~~~~~~~~~~

::

    pysteps-importer-abc        (project name)

For the project name, our example used the following convention:
**pysteps-importer-<institution short name>**.
Note that this convention is not strictly needed, and any name can be used.

Package name
~~~~~~~~~~~~

::

    pysteps-importer-abc
    └── pysteps_importer_abc    (package name)

This is the name of our package containing the new importers for pysteps.
The package name should not contain spaces, hyphens, or uppercase letters.
For our example, the package name is **pysteps_importer_abc**.

\__init__.py
~~~~~~~~~~~~

::

    pysteps-importer-abc
        ├── pysteps_importer_abc
        └───── __init__.py

The __init__.py files are required to inform python that a given directory contains a
python package. This is also the first file executed when the importer plugin
(i.e., the package) is imported.

Importer module
~~~~~~~~~~~~~~~

::

    pysteps-importer-abc
        ├── pysteps_importer_abc
        └───── importer_abc_xyz.py  (importer module)

Inside the package folder (*pysteps_importer_abc*), we place the python module
(or modules) containing the actual implementation of our new importers.
Below, there is an example of an importer module that implements the skeleton of two
different importers (the "grib" and "netcdf" importer that we are using as an example):

.. literalinclude:: importers_module_example.py
   :language: python


setup.py
~~~~~~~~

::

    pysteps-importer-abc        (project name)
    └── setup.py                (Build and installation script)

The `setup.py` file contains all the definitions for building, distributing, and
installing the package. A commented example of a setup.py script used for the plugin
installation is shown next:

.. literalinclude:: example_setup.py
   :language: python


Manifest.in
~~~~~~~~~~~


If you don't supply an explicit list of files, the installation using `setup.py` will
include the minimal files needed for the package to run (the \*.py files, for example).
The Manifest.in file contains the list of additional files and directories to be
included in your source distribution.

Next, we show an example of a Manifest file that containing a README and the LICENSE
files located in the project root. Lines starting with **#** indicate comments, and they
are ignored.

::

    # This file contains the additional files included in your plugin package

    include LICENSE

    include README.rst

    ###You can also add directories with data, tests, etc.
    # recursive-include dir_with_data

    ###Include the documentation directory, if any.
    # recursive-include doc

For more information about the manifest file, see
https://docs.python.org/3/distutils/sourcedist.html#specifying-the-files-to-distribute

Get in touch
============

If you have questions about the plugin implementation, you can get in touch with the
pysteps community on our `pysteps slack`__.
To get access to it, you need to ask for an invitation or use the automatic
invitation page `here`__. This invite page can sometimes take a while to load so, please
be patient.

__ https://pysteps.slack.com/
__ https://pysteps-slackin.herokuapp.com/

