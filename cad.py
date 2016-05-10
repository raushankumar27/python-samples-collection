def anti_vowel(text):
    z=text.lower()
    for x,ind in enumerate(z):
        print(x) 
        if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
            del text[ind]
    return text
 
print(anti_vowel('ABCDE'))