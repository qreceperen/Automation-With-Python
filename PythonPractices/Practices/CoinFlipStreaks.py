'''Write a  program to find out how often a streak of six heads or a streak of six tails comes up randomly generated list of heads and tails.
First, create random heads or tails values. Second check if there is streak in it. Repeat the experiment 10000 times.'''


# 2. put random values in a list
# 3. Check in the list if there is streak (six head or six tails in a row) Find the number of streaks. 
# 1. Create random heads or tails
import random

tries = 0
flipCoinsRecordList = []
numberOfStreak = 0
while tries < 10000:

    flipCoins = random.randint(0,1)
    if flipCoins == 0:
        flipCoinsRecordList.append('H')
    else:
        flipCoinsRecordList.append('T')
    tries +=1
joinflipRecordList = ''.join(flipCoinsRecordList)

# Find number of streaks.
# print(joinflipRecordList) # All flip coins results printed (string)


### K lenght character consecutive count. NEED TO CHECK AGAIN.
K = 6

res = []

for idx, ele in enumerate(joinflipRecordList):

    substr = ele *K  # it multiplies each iteration in the string with K

    if joinflipRecordList[idx : idx + K] == substr: # start from each letter to check K lenght consecutive characters. idx = 0 idx +k = 6. idx =1 idx + K = 7, idx =2 idx +K =8. Check 6 characters portion for each iteration.
        res.append(substr)

print(str(list(res)))


# TRY TO COUNT HOW MANY TTTTTT AND HHHHHH in the list. 