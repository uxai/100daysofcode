import pandas

nato_code = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {data.letter: data.code for _, data in nato_code.iterrows()}

convert = input("Enter a word: ").upper()
nato_translation = [nato_dict[letter] for letter in convert]
print(nato_translation)