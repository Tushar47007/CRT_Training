input_string = input("Enter the string: ")
vowel_count = 0
consonant_count = 0
symbol_count = 0

for i in input_string:
    if(i in 'aeiou'):
        vowel_count+=1
    elif(i in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'):
        consonant_count+=1
    else:
        symbol_count+=1

print("Vowel count:",vowel_count)
print("Consonants count:",consonant_count)
print("Symbol count:",symbol_count)

