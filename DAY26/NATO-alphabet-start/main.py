import pandas

nato_alphabet_data  = pandas.read_csv("day26/NATO-alphabet-start/nato_phonetic_alphabet.csv")

phonetic_dict ={row.letter:row.code for (index,row) in nato_alphabet_data.iterrows()}
# print(phonetic_dict)
text = input("enter your words:").upper()

output_list =[phonetic_dict[letter] for letter in text]
print(output_list)
