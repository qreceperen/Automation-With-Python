#!/usr/bin/env python3
import pyperclip, re

text = ' Hello my name is Recep, my Phone number is 716-507-7610'
phoneRegex = re.compile(r'''(
    (\d{3} | \(d{3}\))? # area code
    (\s|-|\.)           #separator
    (\d{3})             # first 3 digits
    (\s|-|\.)           # separator
    (\d{4})             # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extention
)''',re.VERBOSE)


findPhone = phoneRegex.findall(text)   
print(findPhone)