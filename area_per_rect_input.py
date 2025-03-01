#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date :23-02-2025
# This program calculates the perimeter & area of a rectangle

import math

def main():

    # asks for user input to assign a value for width and length variables
    print("")
    print("what is the width of your rectangle")
    width = float(input(""))

    print("")
    print("what is the length of your rectangle")
    length = float(input(""))

    # calculates the area and perimeter of the rectangle 
    print("")
    print("The Area of your rectangle = {}".format(width * length))
    print("The Perimeter of your rectangle = {}".format(2 * (width + length)))
    

if __name__ == "__main__":
    main()