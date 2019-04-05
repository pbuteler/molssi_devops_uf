"""
molssi_devops_uf
A sample repository for the MolSSI workshop at UF.
"""

# Add imports here
from .molssi_math import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
