"""Conway's Game of Life, the clssical cellular automata simulation"""

import sys, copy, random, time

#Set up the constants
WIDTH = 79 #width fo the cell grid
HEIGHT = 20 #height of the cell grid

ALIVE = '0' #Character representing a living cell
DEAD = ' ' #Character representing dead cell

#the cells and nextCells are dictionairies for the state of the game
#their keys are (x,y) tuples and thier values are one of the ALIVE or DEAD values
nextCells = {}

#Put random dead and alive cells into nextCells
for x in range(WIDTH): #loop over every possible column
    for y in range(HEIGHT): #loop over every possible row
        #50/50 chance for starting cells being alive or dead
        if random.randint(0,1) == 0:
            nextCells[(x,y)] = ALIVE #Adda living cell
        else:
            nextCells[(x,y)] = DEAD

while True: #Main program loop
    #Each iteration of this loop is a step of the simulation

    print('\n' * 50) #Separate each step with newlines
    cells = copy.deepcopy(nextCells)

    #Print cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x,y)], end='') #Print the alive character or space
        print()
    print("Press Ctrl-C to quit")

    #Calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Get the neighboring coordinate of (x.y) even if they wrap around the edge
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            #COunt the number of living neighbors
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1

            #Set cell based on COnway's Game of Life rules
            if cells[(x, y)] == ALIVE and (numNeighbors == 2 or numNeighbors ==3):
                nextCells[(x,y)] = ALIVE
                #Living cells with 2 or 3 neighbors stay alive
            elif cells[(x,y)] == DEAD and numNeighbors == 3:
                #Dead cells with 3 neighbors become alive
                nextCells[(x,y)] = ALIVE
            else:
                #Everything is dead or stays dead
                nextCells[(x,y)] = DEAD

    try:
        time.sleep(1) #Add a one second pause to reduce flickering
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        sys.exit()

