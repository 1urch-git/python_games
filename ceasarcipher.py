"""Caesar cipher is a shift cipher that uses addition and subtraction to encrypt and decrypt letters and messages"""

try:
    import pyperclip #pyperclip copies text to the clipboard
except ImportError:
    pass # if pyperclip is not installed, skip it

#Any possible symbol can be encrypted/decrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print("Caesar Cipher")
print("AKA ROT13 cipher, shifts letters by a certain number")
print()

#Let the user enter if they are encrypting or decrypting
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

#Let the user enter the key to use
while True: #Keep asking until the user enters a valid key
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> '.upper())
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break
#Let the user enter the message to encrypt or decrypt
print('Enter the message to {}'.format(mode))
message = input('> ')

#Caesar cipher only works on uppercase letters
message = message.upper()

#Stores the encrypted/decrypted form of the message
translated = ''

#Encrypt/decrypt each symbol in the message
for symbol in message:
    if symbol in SYMBOLS:
        #Get the encrypted (or decrypted) number for this symbol
        num = SYMBOLS.find(symbol) #get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        #Handle the wrap-around if num is larger than the length of SYMBOLS or less than 0
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        
        #Add encrypted/decrypted number's symbol to translated
        translated = translated + SYMBOLS[num]

    else:
        #Just add the symbol without encrypting/decrypting
        translated = translated + symbol

#Display the encrypted/decrypted string to the screen
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard'.format(mode))
except:
    pass #do nothing if pyperclip isn't installed






