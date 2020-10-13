#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

from pprint import pprint


def test_importers():
    """
    Tests for the importers
    """

    from pysteps.io import interface

    pprint(interface._importer_methods)

    assert True
