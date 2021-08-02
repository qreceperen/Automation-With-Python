print("Enter the English message to translate into Pig latin")
message = input()
VOWELS = ('a','e','i','o','u','y')
pigLatin = []

for word in message.split():

    # Separate the non-letters at the start of this word:
    prefixNonletters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonletters += word[0]
        word = word[1:]
    
    if len(word) == 0:
        pigLatin.append(prefixNonletters)
        continue
    
    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]

    # Remember if the word was in uppercase or title case.
    wasUpper = word.isupper() 
    wasTitle = word.istitle()
    word = word.lower() # Make word lower for translation. upper letters will be called after translation.



    # Separate the consonant at the start of this word.
    prefixConsonant = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonant += word[0]
        word = word[1:]

    # Add the Pig latin ending of the word.
    if prefixConsonant!='':
        word += prefixConsonant + 'ay'
    else:
        word+= 'yay'

    # Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # Add the nonletters back to the start or end of the word.
    pigLatin.append(prefixNonletters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(' '.join(pigLatin))

    # print(word)
