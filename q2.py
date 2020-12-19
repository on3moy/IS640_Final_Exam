"""Write a program q2.py that performs the following tasks:

1)	(50 points) Read the file and create a dictionary that each word in the text file is a key, the value is the line numbers that the word appears in the file. The first line number is 1. If a word appears in a line multiple times, only put the line number once. For example, “it” appears in line 4 two times, only put one “4” as its value.
2)	(50 points) Calculate the frequency of each word appears in the file. For example, “Alice” has a frequency of 2, in line 1 and line6. “it” has a frequency of 2, both in line 4. 
3)	(50 points) Write an output file named “index.txt”. The output is sorted by the key in ascending order: key, frequency and list of line numbers separated by a space. The format is “Key (frequency): line1 line2 line3”. The following is a partial content of the generated “index.txt”: 

Alice (2): 1 6 
beginning (1): 1
book (2): 3 5
…
it (2): 4
…
without (1): 7
"""

# Global Variables
TEXT_FILE = 'alice.txt'
READ_MODE = 'r'
ENCODING = 'utf-8'
OUTPUT_INDEX = 'index.txt'
WRITE_MODE = 'w'

# Check to see if file is in directory
try:
    with open(TEXT_FILE, READ_MODE, encoding=ENCODING) as content:
        word_location = {}
        word_count = {}
        row = 0
        for line in content:
            # Shows which row you are in
            row += 1
            words = line.split()
            for word in words:
                # Get word count
                word_count[word] = word_count.get(word, 0) + 1
                # Get row locations
                word_location[word] = word_location.get(word,str()) + ' ' + str(row)

    # Sort words according to keys in ascending order
    words_sorted = sorted(word_count.items(), key=lambda x : x)
    
    # Create an output to write results
    with open(OUTPUT_INDEX, WRITE_MODE) as text:
        for word, frequency in words_sorted:
            text.write(f'{word} ({frequency}): {word_location[word]}\n')

except FileNotFoundError:
    print(f'File {TEXT_FILE} not found')