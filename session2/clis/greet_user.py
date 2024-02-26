import argparse

# Create a parser object
parser = argparse.ArgumentParser(description='Greet the user')

# Add an argument
parser.add_argument('number', type=int, help='number')

# Parse the arguments
args = parser.parse_args()


# Print the greeting
print(args.number**2)