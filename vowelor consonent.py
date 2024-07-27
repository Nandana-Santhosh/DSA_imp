'''Program to find if a character is vowel or Consonant'''

def vowelorconsonant(x):
    if (x=='a'or x=='e' or x=='i'or x=='o' or x=='u'or x=='A'or x=='E' or x=='I' or x=='O' or x=='U'):
        print('VOWEL')
    else:
        print('CONSONANT')
vowelorconsonant('c')
vowelorconsonant('A')


def isVowel(ch): 
    # Dictionary to map vowels to the string "Vowel"
    switcher = { 
        'a': "Vowel", 
        'e': "Vowel", 
        'i': "Vowel", 
        'o': "Vowel", 
        'u': "Vowel", 
        'A': "Vowel", 
        'E': "Vowel", 
        'I': "Vowel", 
        'O': "Vowel", 
        'U': "Vowel"
    } 
    # Return "Vowel" if ch is in the dictionary, otherwise return "Consonant"
    return switcher.get(ch, "Consonant") 

# Driver Code 
print('a is ' + isVowel('a'))  # Expected output: 'a is Vowel'
print('x is ' + isVowel('x'))  # Expected output: 'x is Consonant'
