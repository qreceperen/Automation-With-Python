#!/usr/bin/env python3
import json


# Upload the json data package that has all words and definitions.
data = json.load(open('/Users/eren/Automation-With-Python/PythonPractices/Dictionary/data.json'))

def translate ():
    word = input("Enter word: \n") # Ask user to search for the word that they want to learn meaning.
    return data[word] # it will return the word in the data.(Dictionary finding)




print(translate())
