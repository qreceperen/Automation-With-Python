#!/usr/bin/env python3 
import random  # we can call random.randint here.
import sys  # we can call sys.exit() here.

print("ROCK, PAPER, SCISSOR")

# keep records of number of wins, loses and ties
wins = 0
loses = 0
ties = 0

while True:  # This is the main game loop.
    print(f'{wins}, Wins, {loses} Loses, {ties} Ties.')
    while True:
        print("Enter your move: (r)ock (p)aper, (s)cissor or (q)uit.")
        playerMove = input()
        if playerMove == "q":
            sys.exit()  # Quit the game.
        if playerMove == 'r' or playerMove == 'p' or playerMove =='s':
            break # Break out the player while loop.
        print("Type one of r,p,s or q") # While loop continue until player chose one of these letter.

    # Display what the player choose:
    if playerMove == 'r':
        print ("ROCK versus...")
    elif playerMove == 'p':
        print ("PAPER versus...")
    elif playerMove == 's':
        print ("SCISSOR versus...")

    # Display what the computer chosess:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print("ROCK")
    elif randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNumber == 3:
        computerMove = 's'
        print("SCISSORS")

    # Compare player Move and Computer move and record the win, loses and ties.

    if playerMove == computerMove:
        print ("It is a tie")
        ties +=1
    elif playerMove == 'r' and computerMove == 's':
        print ("you win!")
        wins +=1
    elif playerMove == 'p' and computerMove == 'r':
        print ("you win!")
        wins +=1

    elif playerMove == 's' and computerMove == 'p':
        print ("you win!")
        wins +=1

    elif playerMove == 'r' and computerMove == 'p':
        print ("you lose!")
        loses +=1

    elif playerMove == 's' and computerMove == 'r':
        print ("you lose!")
        loses +=1
    elif playerMove == 'p' and computerMove == 's':
        print ("you lose!")
        loses +=1
