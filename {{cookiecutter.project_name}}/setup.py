# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

# Add the plugin dependencies here
requirements = []

# Add the packages needed to build the package.
setup_requirements = ['pytest-runner']

test_requirements = ['pytest>=3']

# Custom command to run tests using pytest
def run_tests():
    import pytest
    errno = pytest.main(["tests"])
    raise SystemExit(errno)


{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

entry_label = 'pysteps.plugins.' + '{{ cookiecutter.plugin_type }}'

# It woudld be even better to read the functions from the plugin module.
# We could add multiple functions in the entry_points.
# Is that possible?
# e.g. like plugin_functions = [attr for attr in dir(importlib.import_module(cookiecutter.project_slug.cookiecutter.plugin_type.cookiecutter.plugin_name)) if attr.startswith("import_" if "importer" in cookiecutter.plugin_type else cookiecutter.plugin_type+"_")]
# Then loop over the functions to set all entry_points.
entry = {
    entry_label: [
        '{{ cookiecutter.plugin_function }}={{ cookiecutter.project_slug }}.{{ cookiecutter.plugin_type }}.{{ cookiecutter.plugin_name }}:{{ cookiecutter.plugin_function }}'
    ]
}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    python_requires='>=3.10',
    classifiers=[
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.12'
    ],
    description="{{ cookiecutter.project_short_description }}",
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=readme,
    include_package_data=True,
    keywords=['{{ cookiecutter.project_slug }}', 'pysteps' , 'plugin', '{{ cookiecutter.plugin_type }}'],
    name='{{ cookiecutter.project_name }}',
    packages=find_packages(),
    setup_requires=setup_requirements,
    # Entry points
    # ~~~~~~~~~~~~
    #
    # This is the most important part of the plugin setup script.
    # Entry points are a mechanism for an installed python distribution to advertise
    # some of the components installed (packages, modules, and scripts) to other
    # applications (in our case, pysteps).
    # https://packaging.python.org/specifications/entry-points/
    #
    # An entry point is defined by three properties:
    # - The group that an entry point belongs indicate the kind of functionality that
    #   provides. For the pysteps importers use the "pysteps.plugins.importers" group.
    #   For the pysteps diagnostics use the "pysteps.plugins.diagnostics" group.
    # - The unique name that is used to identify this entry point in the
    #   "pysteps.plugins.importers" group.
    # - A reference to a Python object. For the pysteps importers, the object should
    #   point to a importer function, and should have the following form:
    #   package_name.module:function.
    # The setup script uses a dictionary mapping the entry point group names to a list
    # of strings defining the importers provided by this package (our plugin).
    # The general form of the entry points dictionary is:
    # entry_points={
    #     "group_name": [
    #         "entry_point_name=package_name.module:function",
    #         "entry_point_name=package_name.module:function2",
    #     ]
    # },
    entry_points = entry,
    version='{{ cookiecutter.version }}',
    zip_safe=False,
    cmdclass = {
        'test': run_tests,
    },
)
