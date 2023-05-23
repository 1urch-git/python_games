"""Duckling screensaver"""

import random, shutil, sys, time

#Establish the constants

PAUSE = 0.2
DENSITY = 0.10

DUCKLING_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

#Get the size of the terminal window
WIDTH = shutil.get_terminal_size()[0]
#We can't print to the last column on windows without adding a newline automatically, so reduce by one
WIDTH -= 1


def main():
    print("Duckling Screensaver")
    print("Press Ctrl-C to quit...")
    time.sleep(2)

    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:
        #Main  program loop
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            #See fi we should create a duckling in this lane
            if (ducklingObj == None and random.random() <= DENSITY):
                #Place a duckling in this lane
                ducklingObj = Duckling()
                ducklingLanes[laneNum] = ducklingObj

            if ducklingObj != None:
                #Draw a duckling if there is one in this lane
                print(ducklingObj.getNextBodyPart(), end='')
                #delete the duckling if we've finished drawing it
                if ducklingObj.partToDisplayNext == None:
                    ducklingLanes[laneNum] = None

            else:
                #Draw five spaces since ther is no duckling here
                print(' ' * DUCKLING_WIDTH, end='')

        print()
        sys.stdout.flush()
        time.sleep(PAUSE)


class Duckling:
    def __init__(self):
        """Create a new duckling with random body features"""
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            #Chubby ducklings can only have beady eyes
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])
        
        self.partToDisplayNext = HEAD


    def getHeadStr(self):
        #Returns string of the ducklings head
        headStr = ''
        if self.direction == LEFT:
            #Get the mouth
            if self.mouth == OPEN:
                headStr += '>'
            elif self.mouth == CLOSED:
                headStr += "="

            #get the eyes
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += '" '
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'
            
            headStr += ') ' #Get the back of the head

        if self.direction == RIGHT:

            headStr += ' ('  #Get the back of the head

            #get the eyes
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += ' "'
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            #Get the mouth
            if self.mouth == OPEN:
                headStr += '<'
            elif self.mouth == CLOSED:
                headStr += "="

        if self.body == CHUBBY:
            #Get an extra space so chubby ducklings are the same width as very chubby ducklings
            headStr += ' '
        
        return headStr

    def getBodyStr(self):
        """Returns the string of the duckling's body"""
        bodyStr = '(' #Get left side of body
        if self.direction == LEFT:
            #Get the interior body space
            if self.body == CHUBBY:
                bodyStr += ' '
            if self.body == VERY_CHUBBY:
                bodyStr += '  '
            
            #Get the wing
            if self.wing == OUT:
                bodyStr += ">"
            if self.wing == UP:
                bodyStr += "^"
            if self.wing == DOWN:
                bodyStr += "v"
        if self.direction == RIGHT:
            
            #Get the wing
            if self.wing == OUT:
                bodyStr += "<"
            if self.wing == UP:
                bodyStr += "^"
            if self.wing == DOWN:
                bodyStr += "v"    

            #Get the interior body space
            if self.body == CHUBBY:
                bodyStr += ' '
            if self.body == VERY_CHUBBY:
                bodyStr += '  '

        bodyStr += ')' #Get the right side of the body

        if self.body == CHUBBY:
            #get an extra space so chubby ducklings are the same width as very chubby ducklings
            bodyStr += ' '
        
        return bodyStr

    def getFeetStr(self):
        #return string of duckling's feet
        if self.body == CHUBBY:
            return ' ^^  '
        if self.body == VERY_CHUBBY:
            return ' ^ ^ '
    
    def getNextBodyPart(self):
        """Calls the appropriate display method for the next body part that needs to be displayed; sets partToDisplayNext to None when finished"""
        if self.partToDisplayNext == HEAD:
            self.partToDisplayNext = BODY
            return self.getHeadStr()
        elif self.partToDisplayNext == BODY:
            self.partToDisplayNext = FEET
            return self.getBodyStr()
        elif self.partToDisplayNext == FEET:
            self.partToDisplayNext = None
            return self.getFeetStr()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() #Ctrl-C ends the program





