"""
A game that guesses a number and provides hints along the way
"""

import random

NUM_DIGITS = 3 #number of digits in the sequence
MAX_GUESSES = 10 #number of guesses

def main():

    print("""
    Bagels: A Deductive Logic Game

    I am thinking of a {}-digit number with no repeated digits. Try to guess the number. 
    Here are clues:

    Pico    One digit is correct, but in the wrong position.
    Fermi   One digit is correct and in the correct position.
    Bagels  No digit is correct.

    """.format(NUM_DIGITS)) 

    while True: #Main game loop
        secretNum = getSecretNum()
        print("I am thinking of a number.")
        print("You have {} guesses to get it.".format(MAX_GUESSES))  

        numGuesses = 1

        while numGuesses <= MAX_GUESSES:
            guess = ''
            #Keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input("> ")
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break #the guess is correct, break the loop
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses")
                print("The answer was {}.".format(secretNum))

        #Ask player if they want to play again
        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break
    print("Thanks for playing!")


def getSecretNum():
    
    """Returns a string made up of NUM_DIGITS unique random digits """
    numbers = list('0123456789') #establish the sequence of numbers used
    random.shuffle(numbers) #shuffle them into random order
    #get the first X digits of the string of random numbers for the secret number
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """returns a string with pico, fermi, or bagels clues for the guessing of a secret number """
    if guess == secretNum:
        return "You got it!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            #a correct digit is in the correct place
            clues.append('Fermi')
        elif guess[i] in secretNum:    
            #a digit is in the sequence but not in the correct place
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels'
        #there are no correct digits in the guess

    else:
        #Sort the clues in alphabetical order so they give no indication of correct position
        clues.sort()
        #make a single string from the list of string clues
        return ' '.join(clues)

#If the program is run instead of imported, run the game

if __name__ == '__main__':
    main()


