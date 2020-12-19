"""Write a program that performs the following tasks:

-	(10 points) Set the random seed to 2020 
-	(20 points) Randomly generate 10,000 numbers between 1000 and 2000 (inclusive) 
-	(50 points) Find all numbers that are 
o	even numbers and 
o	can be divided by 7 
-	(50 points) Count the frequency of the above numbers. Tips: you may want to use a dictionary.
-	(20 points) Display the numbers in ascending order and their frequencies as the following (sample output showing the format, not the real result):

1008 17
1022 19
1036 15
…
"""
# Import libraries
import random

# Global Variables
SEED_NUMBER = 2020
NUMBER_TO_GENERATE = 10_000
START_RANGE = 1_000
END_RANGE = 2_000

# Set seed number
random.seed(SEED_NUMBER)

# Define functions
def generate_list(start, end, cycles):
    """Generates a list denpending on arguments"""
    return [random.randrange(start, end + 1) for _ in range(cycles)]

def modify_list(array):
    """Input a list and only show numbers divisible by 2 and 7"""
    result = []
    for number in array:
        if number % 2 == 0 and number % 7 == 0:
            result += [number]
    return result

def frequency_count(array):
    """Input a list and return a dictionary of frequency counts"""
    frequency = {}
    for num in array:
        frequency[num] = frequency.get(num, 0) + 1
    return frequency

def main():
    """Generate a list, modify, sort in ascending order and print out results"""
    generated_list = generate_list(START_RANGE, END_RANGE, NUMBER_TO_GENERATE)

    # Modify list to be divisible by only 7 and 2
    modified_list = modify_list(generated_list)
    
    # Create dictionary with frequency counts
    frequency = frequency_count(modified_list)

    # Sort the dictionary by converting it back to a list
    dictionary_sorted = sorted(frequency.items(), key=lambda x: x[0])

    # print out sorted list
    for number, frequency in dictionary_sorted:
        print(f'{number} {frequency}')
    
main()