cwlVersion: v1.0
class: CommandLineTool
baseCommand: [python, /Users/emily/cwl_demo/python_scripts/reproject.py]

inputs:
  input_vector:   # the vector to reproject
    type: File
    inputBinding:
      position: 1
  epsg_code:      # the EPSG code of the projection to reproject to
    type: int
    inputBinding:
      position: 2
  output_vector:  # the path to write out the reprojected vector
    type: string
    default: reprojected_vector.gpkg
    inputBinding:
      position: 3

outputs:
  reprojected_vector:
    type: File
    outputBinding:
      glob: $(inputs.output_vector)  # refer back to the input path provided
