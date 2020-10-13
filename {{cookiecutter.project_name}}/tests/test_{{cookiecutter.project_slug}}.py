#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""


def test_importers_discovery():
    """It is recommended to at least test that the importers provided by the plugin are
    correctly detected by pysteps. For this, the tests should be ran on the installed
    version of the plugin (and not against the plugin sources).
    """

    from pysteps.io import interface

    assert "import_abc_xxx" in interface._importer_methods
    assert "import_abc_yyy" in interface._importer_methods


def test_importers_with_files():
    """Additionally, you can tests that your importers correctly reads the corresponding
    some example data.
    """

    # Write the test here.
    pass
