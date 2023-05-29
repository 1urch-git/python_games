"""Bouncing DVD logo:
A bouncing DVD logo animation. Press Ctrl-C to stop.

Note: do not resize the terminal window while the program is running. Your computer will explode.
"""

import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install with pip, or go to')
    print('https://pypi.org/project/Bext')
    sys.exit()


#Establish the constants
WIDTH, HEIGHT = bext.size()

#we can't print to the last column on a windows machine without it adding a newline character, so decrease width by one
WIDTH -= 1 

NUMBER_OF_LOGOS = 5 #
PAUSE_AMOUNT = 0.2

COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

#Key names for logo dictionaries
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = "direction"

def main():
    bext.clear()

    #Generate some logos
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
        X: random.randint(1, WIDTH - 4),
        Y: random.randint(1, HEIGHT - 4),
        DIR: random.choice(DIRECTIONS)})

        if logos[-1][X] % 2 == 1:
            #Make sure X is even so it can hit the corner
            logos[-1][X] -= 1

    cornerBounces = 0 #Count how many times a logo hits a corner
    while True: #main program loop
        for logo in logos: #handle each logo in the logos list
            #Erase the logo's current location
            bext.goto(logo[x], logo[y])
            print('   ', end='')

            originalDirection = logo[DIR]

            #Check if the logo bounces off the corner
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT-1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH-3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH-3 and logo[Y] == HEIGHT-1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1
            
            #Check if the logo bounces off of the left edge
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            #Check if the logo bounces off of the right edge
            #WIDTH-3 because DVD has three letters
            elif logo[X] == WIDTH-3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[x] == WIDTH-3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            #Check if the logo bounces off of the top edge
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT


            #Check if the logo bounces off of the bottom edge
            elif logo[Y] == HEIGHT-1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT-1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT
            
            if logo[DIR] != originalDirection:
                #Change the color when the logo bounces
                logo[COLOR] = random.choice(COLORS)

            #Move the logo
            if logo[DIR] == UP_RIGHT:
                logo[x] += 2
                logo[Y] -= 1
            if logo[DIR] == UP_LEFT:
                logo[x] -= 2
                logo[Y] -= 1
            if logo[DIR] == DOWN_RIGHT:
                logo[x] += 2
                logo[Y] += 1
            if logo[DIR] == DOWN_LEFT:
                logo[x] -= 2
                logo[Y] += 1

        #Display number of corner bounces
        bext.goto(5,0)
        bext.fg('white')
        print('Corner Bounces: ', cournerBounces, end='')

        for logo in logos:
            #Draw the logos at their new location
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0,0)

        sys.stdout.flush() #Required for using bext programs
        time.sleep(PAUSE_AMOUNT)

#If this program was run instread of imported, run the game
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Bouncing DVD Logo!")
        sys.exit() #End the program with CTRL-C



