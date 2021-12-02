cwlVersion: v1.0
class: Workflow
doc: |
  An example of using a workflow to join together a series of common
  geospatial data processing operations.

inputs:
  lulc: File
  dem: File
  output_projection_epsg_code: int

outputs:
  processed_lulc:
    type: File
    outputSource: reproject/reprojected_vector


steps:
  resample:
    doc: Resample the LULC to the same resolution as the DEM.
    run: tools/resample_tool.cwl
    in:
      input_raster: lulc
      target_raster: dem
    out: [resampled_raster]

  reclassify:
    doc: Reclassify the resampled LULC using a predefined value map.
    run: tools/reclassify_tool.cwl
    in:
      input_raster: resample/resampled_raster
    out: [reclassified_raster]

  vectorize:
    doc: Vectorize the reclassified LULC.
    run: tools/vectorize_tool.cwl
    in:
      input_raster: reclassify/reclassified_raster
    out: [vectorized]

  reproject:
    doc: Reproject the vectorized data into the desired projection.
    run: tools/reproject_tool.cwl
    in:
      input_vector: vectorize/vectorized
      epsg_code: output_projection_epsg_code
    out: [reprojected_vector]
