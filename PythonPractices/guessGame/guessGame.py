import random # Random module allow the program to pick a number randomly

secretNumber = random.randint(1,20) # machine will pick a number randomly between 1 and 20.
print(secretNumber)
# Ask player to guess 6 times.
for guessTaken in range(1,7):
    print ('Take a guess')
    guess = int(input())
    # range allow us to indent 6 times guess. Following if statements will lead the indentation whether stop or continue before 6 times.

    if guess < secretNumber:
        print ('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break # if the guess is correct if statement stops.
    '''Note: Improve code by adding getting closer or getting far. Compare each guess  with previous one to compare whether guess is closer to secret number or not'''
if guess == secretNumber:
    print('Congrations! You guessed the correct number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
