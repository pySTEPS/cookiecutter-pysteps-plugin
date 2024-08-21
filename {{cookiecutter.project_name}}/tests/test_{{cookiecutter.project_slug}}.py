#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""


def test_plugins_discovery():
    """It is recommended to at least test that the plugin modules provided by the plugin are
    correctly detected by pysteps. For this, the tests should be ran on the installed
    version of the plugin (and not against the plugin sources).
    """

    from pysteps.io import interface as io_interface
    from pysteps.postprocessing import interface as pp_interface

    plugin_type = "{{cookiecutter.plugin_type}}"
    if plugin_type == "importer":
        new_importers = ["{{cookiecutter.plugin_name }}"]
        for importer in new_importers:
            assert importer.replace("import_", "") in io_interface._importer_methods

    elif plugin_type == "postprocessor":
        new_postprocessors = ["{{cookiecutter.plugin_name }}"]
        for postprocessor in new_postprocessors:
            postprocessor.replace("postprocessors_", "")
            if postprocessor.startswith("diagnostics"):
                assert postprocessor in pp_interface._diagnostics_methods
            elif postprocessor.startswith("ensemblestats"):
                assert postprocessor in pp_interface._ensemblestats_methods


def test_importers_with_files():
    """Additionally, you can test that your plugin correctly reads the corresponding
    some example data.
    """

    # Write the test here.
    pass
