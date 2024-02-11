# Import the pandas library for data manipulation
import pandas as pd

# Load the NATO phonetic alphabet data from a CSV file into a pandas DataFrame
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the DataFrame where each letter is mapped to its corresponding NATO code
# This is done by iterating over each row of the DataFrame
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Prompt the user to enter a word and convert it to uppercase to match the dictionary keys
word = input("Enter a word:").upper()

# Create a list of NATO phonetic codes corresponding to each letter in the input word
# This list comprehension checks if each letter is in the nato_dict before attempting to access it
nato_series = [nato_dict[letter] for letter in word if letter in nato_dict]

# Print the list of NATO phonetic codes
print(nato_series)
