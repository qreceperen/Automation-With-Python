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