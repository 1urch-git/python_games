#!/bin/usr/python3

import os, sys

row1 = "[ ] [ ] [ ]\n"
row2 = "[ ] [ ] [ ]\n"
row3 = "[ ] [ ] [ ]\n"

row_value1 = []
row_value2 = []
row_value3 = []
    
def intro():
    print("Welcome to tic-tac-toe! Get 3 in a row to win.\n")
    
def help():
    row_value1 = ["[1] ","[2] ","[3]"]
    row_value2 = ["[4] ","[5] ","[6]"]
    row_value3 = ["[7] ","[8] ","[9]"]
    print("Here is how to play: pick a number from the available spots. The slots are numbered like this...\n")
    
    #add update_board() here
    println(row1, row2, row3)

def show_board():
    print(row1, row2, row3)
    
def assign_values():
    input(
    
if __name__ == "__main__":
    #do something
    show_board()
