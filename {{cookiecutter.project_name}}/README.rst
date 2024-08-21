{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
License
=======
* {{ cookiecutter.open_source_license }}
{% endif %}

Documentation
=============

Here write a short description of the plugin, indicating the importers or postprocessors that it provides.

Installation instructions
=========================

Describe the installation instructions here. For example, how to install the plugin from
the sources (cloning the repository and running `setup.py install`), or using `pip`.

Test the plugin
===============

If a test suite is provided with the plugin, describe how to run the tests.

Credits
=======

- This package was created with Cookiecutter_ and the `pysteps/cookiecutter-pysteps-plugin`_ project template.

.. Since this plugin template is based in the cookiecutter-pypackage template,
it is encouraged to leave the following credits to acknowledge Audrey Greenfeld's work.

- The `pysteps/cookiecutter-pysteps-plugin`_ template was adapted from the cookiecutter-pypackage_
template.

.. _cookiecutter-pypackage: https://github.com/audreyfeldroy/cookiecutter-pypackage

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`pysteps/cookiecutter-pysteps-plugin`: https://github.com/pysteps/cookiecutter-pysteps-plugin
