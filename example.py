import pygeoprocessing
from osgeo import gdal, ogr, osr

# input files
raster_a_path = '/Users/emily/cwl_demo/input/raster_a.tif'
raster_b_path = '/Users/emily/cwl_demo/input/raster_b.tif'
reclass_data_path = '/Users/emily/cwl_demo/input/reclass.csv'

# output files
resampled_raster_a_path = '/Users/emily/cwl_demo/output/resampled_raster_a.tif'
reclassified_raster_a_path = '/Users/emily/cwl_demo/output/reclassified_raster_a.tif'
vectorized_path = '/Users/emily/cwl_demo/output/vectorized.gpkg'
reprojected_vector_path = '/Users/emily/cwl_demo/output/reprojected_vector.gpkg'
epsg_code = 3857

# Resample raster A to the resolution of raster B ############################
raster_b_info = pygeoprocessing.get_raster_info(raster_b_path)

pygeoprocessing.warp_raster(
    base_raster_path=raster_a_path,
    target_pixel_size=raster_b_info['pixel_size'],
    target_raster_path=resampled_raster_a_path,
    resample_method='near'
)


# Reclassify raster A using data from CSV ####################################
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

# Vectorize the reclassified raster ##########################################
raster = gdal.Open(reclassified_raster_a_path)
band = raster.GetRasterBand(1)
wkt = pygeoprocessing.get_raster_info(reclassified_raster_a_path)['projection_wkt']

spatial_ref = osr.SpatialReference()
spatial_ref.ImportFromWkt(wkt)

driver = ogr.GetDriverByName('GPKG')
vector = driver.CreateDataSource(vectorized_path)
layer = vector.CreateLayer('layer', spatial_ref)
field = ogr.FieldDefn('value', ogr.OFTInteger)
layer.CreateField(field)

gdal.Polygonize(band, band, layer, 0)

# Reproject the vector #######################################################
spatial_ref = osr.SpatialReference()
spatial_ref.ImportFromEPSG(epsg_code)
pygeoprocessing.reproject_vector(
    base_vector_path=vectorized_path,
    target_projection_wkt=spatial_ref.ExportToWkt(),
    target_path=reprojected_vector_path,
    driver_name='GPKG')

##############################################################################

print('original data:')
print(pygeoprocessing.raster_to_numpy_array(raster_a_path))

print('after resampling:')
print(pygeoprocessing.raster_to_numpy_array(resampled_raster_a_path))

print('after reclassifying:')
print(pygeoprocessing.raster_to_numpy_array(reclassified_raster_a_path))
