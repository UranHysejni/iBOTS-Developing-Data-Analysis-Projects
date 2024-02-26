import argparse
import pandas as pd
import numpy as np

parser = argparse.ArgumentParser(description='Greet the user')


parser.add_argument('input', type=str, help='First input')

parser.add_argument('output', type=str, help='Second input')

parser.add_argument('transform', type=str, help='Third input')

args=parser.parse_args()

# Load the input

input_array = np.load(args.input)

if args.transform=="normal":

    #Nomalization
    output_array = input_array - np.min(input_array)
    output_array = output_array / np.max(output_array)

elif args.transform=="standard":

    #Standardization
    output_array = (input_array - np.mean(input_array)) / np.std(input_array)

else:
    raise

# Save the transformed array
np.save(args.output, output_array)

