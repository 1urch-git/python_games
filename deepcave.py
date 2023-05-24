
import random, sys, time

#Set up the constants
WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Press Ctrl-C to stop.')
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
    #Dispay the tunnel segment
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))

    #Check for Ctrl-C during the brief pause
    try:
        time.sleep(PAUSE_AMOUNT)
    except:
        sys.exit() #end program

    #Adjust the elft side width:
    diceRoll = random.randint(1,6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth -1 #Decrease left side width
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1 #Increase left side width
    else:
        pass #Do nothing; no change in left side width

    #Adjust the gap width
    diceRoll = random.randint(1,6)
    if diceRoll == 1 and gapWidth > 1:
        gapWidth = gapWidth - 1 #DEcrease gapWidth
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        gapWidth = gapWidth + 1 #Increase gap width
    else:
        pass


