#!/usr/bin/env python3
import time
import sys

indent = 0 # represent number of space from the beginning of line
indentIncreasing = True # Reference point that indentation will increase or not.

try:
    while True:
        print(' ' * indent , end='') # This is multiplication. Multiplies ' ' with indent value.
        print('********') # Print function will come after (same line) with previous print. (end='' provide that)
        time.sleep(0.5) # 0.1 is second. Pause the code for 0.1 second.

        if indentIncreasing:
            indent +=1 # Increasing indent value periodically
            if indent ==20:
                indentIncreasing = False # Stop increasing when indent value reaches 20

        else:
            indent -=1 # Starts decreasing indent value from 20 by 1.
            if indent == 0:
                    indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
