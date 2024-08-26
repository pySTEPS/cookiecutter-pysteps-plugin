# -*- coding: utf-8 -*-
"""
One-line description of this module. E.g.

This is a more extensive description (optional) that describes the readers implemented
in this module and other relevant information.
"""

# Import the needed libraries

### Uncomment the next lines if pyproj is needed for the postprocessor.
# try:
#     import pyproj
#
#     PYPROJ_IMPORTED = True
# except ImportError:
#     PYPROJ_IMPORTED = False

# Function {{ cookiecutter.plugin_name }} to create postprocessing plugins.

# IMPORTANT: The name of the postprocessor should follow the "postprocessor_postprocessorType_postprocessorName"
# naming convention. The "postprocessor_" prefix to the postprocessor name is MANDATORY since it is
# used by the pysteps interface. "postprocessorType" refers to the category of postprocessor e.g. diagnostics, ensemblestats, etc.
# "postprocessorName" refers to a unique identifier name for the postprocessor e.g. prtype, meancalc, etc.
#
# Check the pysteps documentation for examples of postprocessor names that follow this
# convention:
# https://pysteps.readthedocs.io/en/latest/pysteps_reference/io.html#available-diagnostics
#
# The function prototype for the postprocessor's declaration should have the following form:
#
#  def postprocessor_type_xyz(filename, **kwargs):
#
#
# Function arguments
# ~~~~~~~~~~~~~~~~~~
#
# The function arguments should have the following form:
# (filename, keyword1="some_keyword", keyword2=10,...,keywordN="something", **kwargs)
# The `filename` and `**kwargs` arguments are mandatory to comply with the pysteps
# interface. To fine-control the behaviour of the postprocessor, additional keywords can be
# added to the function.
# For example: keyword1="some_keyword", keyword2=10, ..., keywordN="something"
# It is recommended to declare the keywords explicitly in the function to improve the
# readability.
#
#
# Return arguments
# ~~~~~~~~~~~~~~~~
#
# The postprocessor can return whatever argument is needed.
#
#

def {{cookiecutter.plugin_name}}(filename, **kwargs):
      """
      A detailed description of the postprocessor. A minimal documentation is
      strictly needed since the pysteps postprocessor interface expects docstrings.

      For example, the documentation may look like this:

      Carry out functionality x.

      Parameters
        ----------
        filename : str
            Name of the file to be processed.

        keyword1 : str
            Some keyword used to fine control the diagnostic postprocessor behaviour.

        keyword2 : int
            Another keyword used to fine control the diagnostic postprocessor behaviour.

        {extra_kwargs_doc}

      Returns
      -------.
      """
      ####################################################################################
      # Add the code required to run the postprocessor here.
      file = open(filename, "w")
      file.write("hello world")
      file.close()
      return file