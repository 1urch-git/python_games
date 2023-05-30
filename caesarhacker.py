"""Caesar Cipher Hacker"""

print('Caesar Cipher Hacker: brak the caesar cipher')

#User specifies the message to hack
print('Enter the encrypted Caesar cipher message to hack:')
message = input('> ')

#Every possible symbol that can be encrypted or decrypted
#This must match the SYMBOLS used when encrypting the message
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): #Loop through every possible cipher
    translated = ''

    #Decrypt each symbol in the message
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol) #Get symbol number
            num = num - key #Decrypt the number
            
            #Handle the wrap-around if num is less than 0
            if num < 0:
                num = num + len(SYMBOLS)

            #Add decrypted number's symbol to translated
            translated = translated + SYMBOLS[num]
        else:
            #Just add the symbol without decrypting:
            translated = translated + symbol
    #Display the key being tested along with the decrypted text
    print('Key #{}: {}'.format(key, translated))





