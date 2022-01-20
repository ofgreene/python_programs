# A program that solves the equation w + x + y + z = x*x - y*y - 1

import math

def main ():
    print ( "solveW.py")
    print ( "w + x + y + z = x*x - y*y - 1 " )
    print ( "This program solves for w in the above equation" )

    x = float ( input ( "Enter value for x: "))
    y = float ( input ( "Enter value for y: "))
    z = float ( input ( "Enter value for z: "))
    w = float (x*x - y*y - 1 - y -z- x)

    print ("The value of w is", w, "when x equals", x, ", and y equals", y, ", and z equals", z,".")

main()
    
