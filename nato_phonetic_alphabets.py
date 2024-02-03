# Nato phonetic alphabet
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato)


def rec():
    word = input("Enter a word: ").upper()
    try:
        letters = [nato[n] for n in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        rec()
    else:
        print(letters)


rec()
