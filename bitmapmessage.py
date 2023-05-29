import sys 

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

print("Bitmap Message")
print("Enter the message to display with the bitmap")
message = input('> ')
if message == '':
    sys.exit()

#Loop over each line of the bitmap
for line in bitmap.splitlines():
    #loop over each character in the line
    for i, bit in enumerate(line):
        if bit == ' ':
            #print an empty space since there's a space in the bitmap
            print(' ', end='')
        else:
                #print a character from the message
                print(message[i % len(message)], end='')
    print()

