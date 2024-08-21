#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove_file("LICENSE")

plugin_type = "{{ cookiecutter.plugin_type }}".lower()

if plugin_type == "postprocessor":
    shutil.rmtree("{{ cookiecutter.project_slug }}/importer")
else:
    shutil.rmtree("{{ cookiecutter.project_slug }}/postprocessor")
