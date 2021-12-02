import sys
import pygeoprocessing
from osgeo import gdal

# input files
raster_a_path = sys.argv[1]
raster_b_path = sys.argv[2]
reclass_data_path = sys.argv[3]

# output files
resampled_raster_a_path = sys.argv[4]
reclassified_raster_a_path = sys.argv[5]

# Resample raster A to the resolution of raster B
raster_b_info = pygeoprocessing.get_raster_info(raster_b_path)

pygeoprocessing.warp_raster(
    base_raster_path=raster_a_path,
    target_pixel_size=raster_b_info['pixel_size'],
    target_raster_path=resampled_raster_a_path,
    resample_method='near'
)

# Reclassify raster A using data from CSV
value_map = {
    1: 3,
    2: 2,
    3: 1
}

pygeoprocessing.reclassify_raster(
    base_raster_path_band=(resampled_raster_a_path, 1),
    value_map=value_map,
    target_raster_path=reclassified_raster_a_path,
    target_datatype=gdal.GDT_Int16,
    target_nodata=-1
)

print('original data:')
print(pygeoprocessing.raster_to_numpy_array(raster_a_path))

print('after resampling:')
print(pygeoprocessing.raster_to_numpy_array(resampled_raster_a_path))

print('after reclassifying:')
print(pygeoprocessing.raster_to_numpy_array(reclassified_raster_a_path))
