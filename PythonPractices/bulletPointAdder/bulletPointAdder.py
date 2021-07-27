#!/usr/bin/env python3

import pyperclip

text = pyperclip.paste() # paste when something copied to the clipboard.

# Separate the lines (identify /n and separate from there)

lines = text.split('\n')
for i in range(len(lines)): # Count the lines and go through.
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text) # Copy the clipboard after editing