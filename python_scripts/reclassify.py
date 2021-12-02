import sys
import pygeoprocessing
from osgeo import gdal

input_path = sys.argv[1]
output_path = sys.argv[2]

# Reclassify raster A values ####################################
value_map = {
    1: 3,
    2: 2,
    3: 1
}

pygeoprocessing.reclassify_raster(
    base_raster_path_band=(input_path, 1),
    value_map=value_map,
    target_raster_path=output_path,
    target_datatype=gdal.GDT_Int16,
    target_nodata=-1
)
