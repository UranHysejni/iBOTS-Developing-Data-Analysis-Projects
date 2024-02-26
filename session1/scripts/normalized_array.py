import sys
import numpy as np
import os
import pathlib

# Command-line inputs
input_array_path = sys.argv[1] # grab the first input
output_array_path = sys.argv[2] # grab the second input

# Load the input and standardize it
input_array = np.load(input_array_path)
output_array = (input_array) / np.abs(np.max(input_array) - np.min(input_array))
path=pathlib.Path(output_array_path)
#os.mkdir(path.parent)
# Save the standardized array
np.save(output_array_path, output_array)