'''
This program converts a user-inputted word into a sequence of 
words based on the NATO phonetic alphabet. For each letter in the input, 
the program looks up and outputs the corresponding NATO phonetic term, creating a set of 
phonetic words that spell out the original word letter by letter.
'''

#Importing pandas module 
import pandas

#Opening csv file containing nato phonetic alphabet 
data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Creates a dictionary from a DataFrame, mapping row.letter to row.code for each row.
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#List of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(result)
#Function call
generate_phonetic()