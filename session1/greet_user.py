
import sys

# Get the number through argument passed in the console
# NOTE that we need to turn it into an integer (by default it is a string)
number = int(sys.argv[1])
number2= int(sys.argv[2])
# Perform the operation
number_sum = number + number2

# print the name
print(f"sum of  {number} and {number2} is {number_sum}.")