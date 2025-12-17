student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


phonetic_data = pandas.read_csv("./nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (idx, row) in phonetic_data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [phonetic_dict[char] for char in word]
    except KeyError:
        print("Sorry, only letters allowed.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()