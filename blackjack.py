"""
Blackjack, aka 21
"""

import sys, random

#Set up the constants, i.e. the unicode code points of the card symbols

HEARTS = chr(9829) #heart character
DIAMONDS = chr(9830) #diamond character
SPADES = chr(9824) #spade character
CLUBS = chr(9827) #club character 
BACKSIDE = 'backside'

def main():
    print("""Blackjack, the card game
    
    Rules:
        Try to get as close to 21 without going over. 
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth thier face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.""")

    money = 5000
    while True: #main game loop
        #Check if the player has money left
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money")
            print("Thanks for playing!")
            sys.exit()
        #Let the player enter their bet for this round
        print("Money: ", money)
        bet = getBet(money)

        #Give the dealer and player two cards from the deck each:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        #Handle player actions
        print("Bet: ", bet)
        while True: #keep looping until player stands or busts
            displayHands(playerHand, dealerHand, False)
            print()

            #Check if the player has bust
            if getHandValue(playerHand) > 21:
                break

            #get the player's move, either H, S, or D
            move = getMove(playerHand, money - bet)

            #Handle the player actions
            if move == "D":
                #Player is doubling down, they can increase thier bet
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print("Bet increased to {}.".format(bet))
                print('Bet: ', bet)

            if move in ('H', 'D'):
                #Hit/Doubling down takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    #The player has busted
                    continue

            if move in ('S', 'D'):
                    #stand/doubling down stops the player's turn
                    break

        #Handle the dealer's actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                #The dealer hits
                print("Dealer hits...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                input("Press Enter to continue...")
                print('\n\n')

        #Show the final hands
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        #Handle whether the player won lost or tied
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("You lost!")
            money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you')

        input('Press Enter to continue...')
        print('\n\n')

def getBet(maxBet):

    """ Ask the player how much they want to bet for this round"""
    while True:
        #keep asking until they give a valid amount
        print('How much do you want to bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if not bet.isdecimal():
            continue #if the didn't enter a number, ask again
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K'):
            deck.append((rank, suit)) #add the face value of the cards
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards Hide the dealer's first card if showDealerHand is False"""
    print()
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        #Hide the dealer's first card
        displayCards([BACKSIDE] + dealerHand[1:])

    #Show the player's cards
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):

    """Returns the value of the cards. Face cards are worth 10, aces 11 or 1, (this function picks the most suitable ace value)."""
    value = 0
    numberOfAces = 0

    #Add the value for the non-ace cards
    for card in cards:
        rank = card[0] #card is a tuple like (rank, suit)
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10 #face cards are worth 10 points
        else:
            value += int(rank) #number cards are worth their face value

    #Add the value for the aces
    value += numberOfAces #Add one per ace
    for i in range(numberOfAces):
        #If another 10 can be added wihtout busting do so
        if value + 10 <= 21:
            value += 10

    return value

def displayCards(cards):
    """Display all the cards in the cards list"""
    rows = ['','','','',''] #the text to display on each row

    for i, card in enumerate(cards):
        rows[0] += '___  ' #print top line of card
        if card == BACKSIDE:
            #print a card's back
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            #print the card's front
            rank, suit = card #the card is a tuple structure
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    
    #Print each row on the screen
    for row in rows:
        print(row)

def getMove(playerHand, money):
    """Ask the player for their move, and returns H for Hit, S for Stand, D for Double down"""
    while True: #keep looping until the player enters a correct move
        #Determine what moves the player can make:
        moves = ['H', 'S', 'D']

        #The player can double down on their first move, which we can tell because they'll have exactly two cards
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        #Get the player's move 
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move #player has entered a valid move
        if move == 'D' and '(D)ouble down' in moves:
            return move #Player has entered a valid move


#If the program is run instead of imported, run the game
if __name__ == '__main__':
    main()




















        