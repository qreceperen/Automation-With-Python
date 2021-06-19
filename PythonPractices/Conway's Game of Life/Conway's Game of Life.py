#!/usr/bin/env python3
import random, time, copy

WIDTH = 60
HEIGHT = 20

# Create List of List to store location (Ellaborate it)

nextCell = []
for x in range(WIDTH):
    column = [] # It will create number of column related to width and store in column list.
    for y in range (HEIGHT): # This nested condition will create y coordinates (HEIGHT) for each x coordinates(WIDTH)
        if random.randint(0,1) == 1: # Hastag (#) represent the living cell. There is a 50/50 chance cell will start live or dead.
            column.append('#')
        else:
            column.append(' ')

    # Next Cell represent all the column. Game coordinates according to WIDTH and HEIGHT is created and coordinates stored in nextCell.
    # Each column generated up nested condition and created list is moved to the nextCell. Process start again. It will contiune to create all WIDTH (60) and HEIGHT (20).
    nextCell.append(column)

# print(nextCell[3]) # DELETE END OF THE CODE!!!! you can try and see next cell.

while True: # Main Program Loop.
    print('/n/n/n/n/n') # Separate each step with new lines.
    # currentCell creates the game table (Coordinates again and again WHY? IS IT REALY THE ITS FUNCTION? nextCell will be copied in to current cell continiously in order to compare with previous cells(I THINK !!!???))
    currentCell = copy.deepcopy(nextCell) # Deepcopy is technical issue. Generally it is used if a list consist another list. nextCell has X and Y coordinates. Each Y number is stored under X numbers' list. 







