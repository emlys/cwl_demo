import sys
import pygeoprocessing
from osgeo import osr

input_path = sys.argv[1]
epsg_code = int(sys.argv[2])
output_path = sys.argv[3]

# Reproject the vector #######################################################
spatial_ref = osr.SpatialReference()
spatial_ref.ImportFromEPSG(epsg_code)
pygeoprocessing.reproject_vector(
    base_vector_path=input_path,
    target_projection_wkt=spatial_ref.ExportToWkt(),
    target_path=output_path,
    driver_name='GPKG')
