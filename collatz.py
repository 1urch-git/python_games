"""Collatz Sequence; generates numbers for the collatz sequence, given a starting number"""

import sys, time

intro = '''
Collatz Sequence, or, the 3n+1 Problem
The Collatz Sequence is a sequence of numbers produced from a starting number n, following three rules:
1) If n is even, the next number is n is n/2
2) If n is odd, the next number n is 3*n + 1
3) If n is 1, stop. Otherwise, repeat.
'''
print(intro)
print('Enter a starting number (greater than 0) or QUIT:')
response = input('> ')

if not response.isdecimal() or response == '0':
    print('You must enter an integer greater than 0.')
    sys.exit()

n = int(response)
print(n, end='', flush=True)
while n != 1:
    if n % 2 == 0: #If n is even
        n = n // 2
    else: #If n is odd
        n = 3*n +1
    
    print(', ' + str(n), end='', flush=True)
    time.sleep(0.1)
print()
