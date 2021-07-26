#!/usr/bin/env python3
# python3 /Users/eren/Automation-With-Python/PythonPractices/mclip/mclip.py

TEXT = {'agree':'''Yes, I agree. That sounds fine to me.''',
        'busy':'''Sorry, can we do this later this week or next week?''',
        'upsell':'''Would you consider making this a monthly donation'''}

import sys
import pyperclip

if len(sys.argv)< 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text ')
    sys.exit()
# Store the keyphrase as string in the variable keyphrase, 
keyphrase = sys.argv[1] # First command line argument.argv[0] is the script name (mclip.py)

if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase]) # copied the value in the dictionar from corresponded key.
        print('Text for ' + keyphrase + ' copied to clipboard.')
else:
        print('There is no text for ' + keyphrase )
