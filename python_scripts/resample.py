import sys
import pygeoprocessing

# input files
raster_a_path = sys.argv[1]
raster_b_path = sys.argv[2]
output_path = sys.argv[3]

# Resample raster A to the resolution of raster B ############################
raster_b_info = pygeoprocessing.get_raster_info(raster_b_path)

pygeoprocessing.warp_raster(
    base_raster_path=raster_a_path,
    target_pixel_size=raster_b_info['pixel_size'],
    target_raster_path=output_path,
    resample_method='near'
)
