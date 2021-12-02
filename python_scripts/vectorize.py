import sys
import pygeoprocessing
from osgeo import gdal, osr, ogr

input_path = sys.argv[1]
output_path = sys.argv[2]

# Vectorize the reclassified raster ##########################################
raster = gdal.Open(input_path)
band = raster.GetRasterBand(1)
wkt = pygeoprocessing.get_raster_info(input_path)['projection_wkt']

spatial_ref = osr.SpatialReference()
spatial_ref.ImportFromWkt(wkt)

driver = ogr.GetDriverByName('GPKG')
vector = driver.CreateDataSource(output_path)
layer = vector.CreateLayer('layer', spatial_ref)
field = ogr.FieldDefn('value', ogr.OFTInteger)
layer.CreateField(field)

gdal.Polygonize(band, band, layer, 0)
