def main():
    print("Diamonds ASCII-art")
    for diamondSize in range (0,15):
        displayOutlineDiamond(diamondSize)
        print() #Print new line
        displayFilledDiamond(diamondSize)
        print() #Print new line

def displayOutlineDiamond(size):
    for i in range(size): #Display top of diamond
        print(' ' * (size - i - 1), end='') #Left side of space
        print('/', end='') #left side of diamond
        print(' ' * (i*2), end='') #Interior of diamond
        print('\\') #right side of diamond

    for i in range(size): #display bottom of diamond
        print(' ' * i, end='') #left side of space
        print('\\', end='') #left side of diamond
        print(' ' * ((size - i - 1) * 2), end='')
        print('/')


def displayFilledDiamond(size):
    #display top half of diamond
    for i in range(size):
        print(' ' * (size - i - 1), end='') #left side of space
        print('/' * (i+1), end='') #left half of diamond
        print('\\' * (i+1)) #right half of diamond
    
    #display bottom half of diamond
    for i in range(size):
        print(' ' * i, end='') #left side of space
        print('\\' * (size - i), end='') #left side of diamond
        print('/' * (size - i)) #right side of diamond

#IF this program was run instead of imported, run the game
if __name__ == '__main__':
    main()





