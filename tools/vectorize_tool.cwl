cwlVersion: v1.0
class: CommandLineTool
baseCommand: [python, /Users/emily/cwl_demo/python_scripts/vectorize.py]

inputs:
  input_raster:   # the raster to vectorize
    type: File
    inputBinding:
      position: 1
  output_vector:  # the path to write out the vector
    type: string
    default: vectorized.gpkg
    inputBinding:
      position: 2

outputs:
  vectorized:
    type: File
    outputBinding:
      glob: $(inputs.output_vector)  # refer back to the input path provided
