"""Snail Race"""

import random, time, sys

#Set p the constants

MAX_NUM_SNAILS = 8
MAX_NAME_LENGTH = 20
FINISH_LINE = 40

print("""Snail Race

@v  <-- snail""")

#Ask how many snails will race

while True:
    #Kepp asking until the player enters a number
    print("How many snails will race? Max: ", MAX_NUM_SNAILS)
    response = input('> ')
    if response.isdecimal():
        numSnailsRacing = int(response)
        if 1 < numSnailsRacing<= MAX_NUM_SNAILS:
            break
    print('Enter a number between 2 and ', MAX_NUM_SNAILS)

#Enter the names of each snail
snailNames = []
for i in range(1, numSnailsRacing+1):
    while True:
        print('Enter snail #' + str(i) + "'s name...")
        name = input('> ')
        if len(name) == 0:
            print("Please enter a name")
        elif name in snailNames:
            print('Choose a different name')
        else:
            break
    snailNames.append(name)

#Display each snail name ont he start line
print('\n' * 40)
print('START' + (' ' * (FINISH_LINE - len('START')) + 'FINISH'))
print('|' + (' ' * (FINISH_LINE - len('|')) + '|'))
snailProgress = {}
for snailName in snailNames:
    print(snailName[:MAX_NAME_LENGTH])
    print('@v')
    snailProgress[snailName] = 0

time.sleep(1.5) #pause before ther ace begins

while True:
    #pick rnaodm snails to move forward
    for i in range(random.randint(1, numSnailsRacing // 2)):
        randomSnailName = random.choice(snailNames)
        snailProgress[randomSnailName] += 1

        #Check is there is a winner
        if snailProgress[randomSnailName] == FINISH_LINE:
            print(randomSnailName, 'has won!')
            sys.exit()

    time.sleep(0.5)
    print('\n' * 40)

    #Display start and finish lines
    print('START' + (' ' * (FINISH_LINE - 1) + '|'))
    print('|' + (' ' * (FINISH_LINE - 1) + '|'))

    #display snails with nametags
    for snailName in snailNames:
        spaces = snailProgress[snailName]
        print((' ' * spaces) + snailName[:MAX_NAME_LENGTH])
        print(('.' * snailProgress[snailName]) + '@v')







