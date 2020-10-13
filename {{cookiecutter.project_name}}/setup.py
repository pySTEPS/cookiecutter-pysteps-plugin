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

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="{{ cookiecutter.project_short_description }}",
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description=readme,
    test_suite='tests',
    tests_require=test_requirements,
    include_package_data=True,
    keywords=['{{ cookiecutter.project_slug }}', 'pysteps' , 'plugin', 'importer'],
    name='{{ cookiecutter.project_name }}',
    packages=find_packages(),
    setup_requires=setup_requirements,
    # In the entry points below, add the importers included in this package.
    # entry_points: dictionary mapping entry point group names to a list of strings defining the plugins provided by this package.
    # The entry point for pysteps importers is "pysteps.plugins.importers".
    entry_points={
        'pysteps.plugins.importers': [
            'import_abc_yyy={{ cookiecutter.project_slug }}:{{ cookiecutter.importer_name }}.import_abc_yyy',
            'import_abc_zzz={{ cookiecutter.project_slug}}:{{ cookiecutter.importer_name }}.import_abc_zzz',
        ]
    },
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
