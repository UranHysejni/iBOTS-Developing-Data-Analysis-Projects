import sys
import pandas as pd
import argparse


parser = argparse.ArgumentParser(description='Greet the user')
# Defining the first argument
parser.add_argument('input', type=str, help='First input')

# Defining the second argument
parser.add_argument('output', type=str, help='Second input')

# Parse the arguments
args = parser.parse_args()

# Load the csv file and extract active trials
df = pd.read_csv(args.input)
df_valid = df[df.valid].copy()

# Save the new dataframe as a csv file
df_valid.to_csv(args.output, index=False)