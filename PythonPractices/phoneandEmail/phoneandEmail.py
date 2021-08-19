#!/usr/bin/env python3
import pyperclip, re

text = ' Hello my name is Recep, my Phone number is 716-507-7610 and my email adress is chemrcperen@gmail.com and eren123@bascs.org'

# Cretat phome Regex
phoneRegex = re.compile(r'''(
    (\d{3} | \(d{3}\))? # area code
    (\s|-|\.)           #separator
    (\d{3})             # first 3 digits
    (\s|-|\.)           # separator
    (\d{4})             # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extention
)''',re.VERBOSE)

# Create e-mail regex
# emailRegex = re.compile(r'''(
#     [a-zA-Z0-9._%+-]+  # User Name
#     @                  # symbol
#     [a-zA-Z0-9.-]+     # Domain Name
#     (\.[a-zA-Z]{2-4})  # dot - something
#     )''',re.VERBOSE)
emailRegex = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+') # Alternate email Regex if above does not work.

# Find matches in clipboard text. 
text = str(pyperclip.paste()) # Take the copied text from clipboard.

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups)


# Copy Results to the Clipboard

if len (matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else: 
    print('No phone Numbers or email addresses found')


