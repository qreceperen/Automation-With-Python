'''Write a  program to find out how often a streak of six heads or a streak of six tails comes up randomly generated list of heads and tails.
First, create random heads or tails values. Second check if there is streak in it. Repeat the experiment 10000 times.'''


# 2. put random values in a list
# 3. Check in the list if there is streak (six head or six tails in a row) Find the number of streaks. 
# 1. Create random heads or tails
import random

tries = 0
flipCoinsRecordList = []
numberOfStreak = 0
while tries < 10:

    flipCoins = random.randint(0,1)
    if flipCoins == 0:
        flipCoinsRecordList.append('H')
    else:
        flipCoinsRecordList.append('T')
    tries +=1
joinflipRecordList = ''.join(flipCoinsRecordList)

# Find number of streaks.
print(type(joinflipRecordList))
print(joinflipRecordList)




# python count letter streaks in string Buradan arastirmaya devam et. 
