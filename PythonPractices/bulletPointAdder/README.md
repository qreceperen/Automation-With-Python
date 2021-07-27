# ADDING BULLETS TO WIKI MARKUP
## Purpose : Add bulletin mark at the beggining of the articles 

## Details 
bulletPointAdder.py will get text from the clipboard, add a star and space to the beginning of each line, and then paste this new text to the clipboard. For Example, If you copied the following text (for Wikipedia article "List of Lists of Lists" to the Clipboard)
    
    Lists of animals
    Lists of aquarium life
    Lists of biologists by author abbreviation
    Lists of cultivates
    -----------------------------------------
    * Lists of animals
    * Lists of aquarium life
    * Lists of biologists by author abbreviation
    * Lists of cultivates

## How it works

1. Copy the paragraph or set of lines
2. Run the program
3. Paste wherever you want.

## Building Notes

    1. We want bulletPointAdder.py to do the followings
        a. Paste from the clipboard
        b. Do something to it.
        c. Copt the new text to the clipboard.
    2. Program seperates each line with '/n' (new line representative)
    
