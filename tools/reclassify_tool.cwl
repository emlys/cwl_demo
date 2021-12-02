cwlVersion: v1.0
class: CommandLineTool
baseCommand: [python, /Users/emily/cwl_demo/python_scripts/reclassify.py]

inputs:
  input_raster:   # the raster to resample
    type: File
    inputBinding:
      position: 1
  output_raster:  # the path to write out the reclassified raster
    type: string
    default: reclassified_raster.tif
    inputBinding:
      position: 2

outputs:
  reclassified_raster:
    type: File
    outputBinding:
      glob: $(inputs.output_raster)  # refer back to the input path provided
