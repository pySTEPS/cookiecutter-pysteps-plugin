# -*- coding: utf-8 -*-
"""
Importer pluging module
"""
import numpy as np


### Uncomment the next lines if pyproj is needed for the importer.
# from pysteps.exceptions import MissingOptionalDependency
# try:
#     import pyproj
#
#     PYPROJ_IMPORTED = True
# except ImportError:
#     PYPROJ_IMPORTED = False

def add_postprocess_keywords(**keywords):
    """
    Add the Postprocessing keywords used by the pysteps.decorator.postprocess_import
    decorator, used to control the default behavior of the importer.

    Operations:
        - Allow type casting (dtype keyword)
        - Set invalid or missing data to predefined value (fillna keyword)

    The following optional keywords arguments are available:

    Parameters
    ----------
    dtype : str
        Default data type for precipitation. Double precision by default.
    fillna : float or np.nan
        Default value used to represent the missing data ("No Coverage").
        By default, np.nan is used.
    """

    def _postprocess_import(importer):
        importer.postprocess_kws = keywords
        return importer

    return _postprocess_import


################## Write your importers below this line ##################################

# The importers added below this function needs to be added in the
# "entry_points" keywords in the setup.py file.
#
# For example, if the import_abc_yyy and import_abc_zzz are included in this file
# the corresponding entry points are:
#
# entry_points={
#         'pysteps.plugins.importers': [
#             'import_abc_yyy={{ cookiecutter.project_slug }}:{{ cookiecutter.importer_name }}.import_abc_yyy',
#             'import_abc_zzz={{ cookiecutter.project_slug}}:{{ cookiecutter.importer_name }}.import_abc_zzz',
#         ]
#     },

# Function to import files the `institution_format` format.
# The @add_postprocess_keywords decorator is strictly needed to
# the add the postprocessing arguments as a function attribute.
# IMPORTANT: The name of the importer should follow the "importer_institution_format"
# naming convention, where "institution" is the acronym or short-name of the institution.
# The "importer_" prefix to the importer name is MANDATORY, since is used by the pysteps
# interface.
#
# Check the pysteps documentation for examples of importers names that follow this convention.
# https://pysteps.readthedocs.io/en/latest/pysteps_reference/io.html#available-importers
@add_postprocess_keywords(dtype="float32")
def import_abc_yyy(filename, keyword1="some_keyword", keyword2=10, **kwargs):
    """Import a precipitation field from a given institution (abc) in a given format (yyy).
    NOTE: the documentation is strictly needed, since pysteps importers expect docstrings.

    Parameters
    ----------
    filename : str
        Name of the file to import.

    keyword1 : str
        Some keyword used to fine control the importer behavior.

    keyword2 : int
        Anohter keyword used to fine control the importer behavior.

    {extra_kwargs_doc}

    ######################################################################################
    # IMPORTANT: Remove these lines in the final version of this function                #
    # The {extra_kwargs_doc} above is needed to add default keywords added to this       #
    # importer by the pysteps.decorator.postprocess_import decorator.                    #
    ######################################################################################

    Returns
    -------
    precipitation : 2D array, float32
        Precipitation field in mm/h. The dimensions are [latitude, longitude].
    quality : 2D array or None
        If no quality information is available, set to None.
    metadata : dict
        Associated metadata (pixel sizes, map projections, etc.).
    """

    ### Uncomment the next lines if pyproj is needed for the importer.
    # if not PYPROJ_IMPORTED:
    #     raise MissingOptionalDependency(
    #         "pyproj package is required to import "
    #         "FMI's radar reflectivity composite "
    #         "but it is not installed"
    #     )

    # Add the code to read the precipitation data (cartesian grid!) here.
    precip = np.zeros((100, 100))
    quality = None

    # Adjust the metadata fields according to the file format specifications.
    # For additional information on the metadata fields, see:
    # https://pysteps.readthedocs.io/en/latest/pysteps_reference/io.html#pysteps-io-importers
    metadata = dict(
        xpixelsize=1,
        ypixelsize=1,
        unit="mm/h",
        transform=None,
        zerovalue=0,
        institution='The institution that create the file',
        projection='+proj=stere +lon_0=25E +lat_0=90N +lat_ts=60 +a=6371288 +x_0=380886.310 +y_0=3395677.920 +no_defs',
        yorigin="upper",
        threshold=0.03,
        x1=0,
        x2=100,
        y1=0,
        y2=100,
    )
    return precip, quality, metadata


# Add a second importer for an additional format
@add_postprocess_keywords(dtype="float32")
def import_abc_zzz(filename, keyword1="some_keyword", keyword2=10, **kwargs):
    """Import a precipitation field from a given institution (abc) in another format (zzz).
    NOTE: the documentation is strictly needed, since pysteps importers expect docstrings.

    Parameters
    ----------
    filename : str
        Name of the file to import.

    keyword1 : str
        Some keyword used to fine control the importer behavior.

    keyword2 : int
        Anohter keyword used to fine control the importer behavior.

    {extra_kwargs_doc}

    ######################################################################################
    # IMPORTANT: Remove these lines in the final version of this function                #
    # The {extra_kwargs_doc} above is needed to add default keywords added to this       #
    # importer by the pysteps.decorator.postprocess_import decorator.                    #
    ######################################################################################


    Returns
    -------
    precipitation : 2D array, float32
        Precipitation field in mm/h. The dimensions are [latitude, longitude].
    quality : 2D array or None
        If no quality information is available, set to None.
    metadata : dict
        Associated metadata (pixel sizes, map projections, etc.).
    """

    ### Uncomment the next lines if pyproj is needed for the importer.
    # if not PYPROJ_IMPORTED:
    #     raise MissingOptionalDependency(
    #         "pyproj package is required to import "
    #         "FMI's radar reflectivity composite "
    #         "but it is not installed"
    #     )

    # Add the code to read the precipitation data (cartesian grid!) here.
    precip = np.zeros((100, 100))
    quality = None

    # Adjust the metadata fields according to the file format specifications.
    # For additional information on the metadata fields, see:
    # https://pysteps.readthedocs.io/en/latest/pysteps_reference/io.html#pysteps-io-importers
    metadata = dict(
        xpixelsize=1,
        ypixelsize=1,
        unit="mm/h",
        transform=None,
        zerovalue=0,
        institution='The institution that create the file',
        projection='+proj=stere +lon_0=25E +lat_0=90N +lat_ts=60 +a=6371288 +x_0=380886.310 +y_0=3395677.920 +no_defs',
        yorigin="upper",
        threshold=0.03,
        x1=0,
        x2=100,
        y1=0,
        y2=100,
    )
    return precip, quality, metadata
