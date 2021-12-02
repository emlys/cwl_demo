#!/usr/bin/env cwl-runner

cwlVersion: v1.0
class: CommandLineTool
baseCommand: [python, example_2.py]
inputs:
  input_raster:
    type: File
    inputBinding:
      position: 1
  resample_raster:
    type: File
    inputBinding:
      position: 1
  reclassification_table:
    type: File
    inputBinding:
      position: 1

outputs: []
