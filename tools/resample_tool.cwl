cwlVersion: v1.0
class: CommandLineTool
baseCommand: [python, /Users/emily/cwl_demo/python_scripts/resample.py]

inputs:
  input_raster:   # the raster to resample
    type: File
    inputBinding:
      position: 1
  target_raster:  # the raster whose pixel size to resample to
    type: File
    inputBinding:
      position: 2
  output_raster:  # the path to write out the resampled raster
    type: string
    default: resampled_raster.tif
    inputBinding:
      position: 3

outputs:
  resampled_raster:
    type: File
    outputBinding:
      glob: $(inputs.output_raster)  # refer back to the input path provided
