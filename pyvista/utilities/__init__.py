"""Utilities routines."""
from .errors import (
    GPUInfo,
    Observer,
    Report,
    assert_empty_kwargs,
    get_gpu_info,
    send_errors_to_logging,
    set_error_output_file,
    check_valid_vector,
    VtkErrorCatcher,
)
from .features import *
from .fileio import *
from .geometric_objects import *
from .helpers import *
from .parametric_objects import *
from .sphinx_gallery import Scraper, _get_sg_image_scraper
from .regression import compare_images
from . import transformations
from .xvfb import start_xvfb
from .reader import (
    get_reader,
    BaseReader,
    BinaryMarchingCubesReader,
    BYUReader,
    CGNSReader,
    EnSightReader,
    FacetReader,
    OBJReader,
    OpenFOAMReader,
    Plot3DMetaReader,
    PLYReader,
    PointCellDataSelection,
    PVDDataSet,
    PVDReader,
    STLReader,
    TimeReader,
    VTKDataSetReader,
    VTKPDataSetReader,
    XMLImageDataReader,
    XMLPImageDataReader,
    XMLRectilinearGridReader,
    XMLPRectilinearGridReader,
    XMLUnstructuredGridReader,
    XMLPUnstructuredGridReader,
    XMLPolyDataReader,
    XMLStructuredGridReader,
    XMLMultiBlockDataReader,
)
