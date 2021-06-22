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
    print('\n\n\n\n') # Separate each step with new lines.
    # currentCell creates the game table
    # currentCell will be printed on screen, necessary calculation will be held on current Cell (Dead cell , live cell etc), 
    currentCells = copy.deepcopy(nextCell) # Deepcopy is technical issue. Generally it is used if a list consist another list. nextCell has X and Y coordinates. Each Y number is stored under X numbers' list. 

    # Printing a specific cell (one cell)
    for y in range(HEIGHT): # It goes line by line( 1st row on X coordinate and 2nd row , 3rd row etc.  )
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # currentCell [x][y] will find a specific one cell, located in currentCells [x][y] location. end allow the print line to continue on one line. 
        print() # It prints a new line at the end of the code.

    # Calculate the next step's cell based on the current step cells:
    for x in range(WIDTH):
        for y in range (HEIGHT):
            # Gete neightboring coordinates
            # '%WIDTH' ensures leftCoord is always between 0 and WIDTH -1. Basically it provides to go out of the coordinates.
            leftCoord = (x-1)%WIDTH
            rightCoord = (x+1)%WIDTH
            aboveCoord = (y-1)%HEIGHT
            belowCoord = (y+1)%HEIGHT

            # Calculate the number of living neighbors.
            numNeighbors = 0

            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors+=1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors+=1 # Top neighbor is alive.    
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors+=1 #  Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors+=1 #  Left neigbor neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors+=1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors+=1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors+=1 #  Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors+=1 #  Bottom-right neighbor is alive.

            # Evaluate the conditions according to number of dead and alive cells.

            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors ==3):
                # 2 or 3 living cell neighbors will stay alive.
                nextCell[x][y]=='#'
            elif currentCells [x][y] == ' ' and numNeighbors ==3:
                # Dead cell with a 3 neighbors will become alive.
                nextCell[x][y] == '#'
            else:
                # Everything else dies or stays dead.
                nextCell[x][y] == ' '
        time.sleep(1) # Reduce flickering by pausing 1 second.







