#! python3
# Ch.10 - Debugging: Raising Exceptions (page 216)

""" 
Here we've defined a boxPrint() function that takes a character, a width, and heigth, and uses the character
to print a little picture of a box with that width and height. This box shape is printed to the screen.

This program uses the except Exception as err form of the except statement. If an Exception object is returned
from boxPrint() (lines 13, 15, 17), this except statement will store it in a variable called err. The Exception
object can then be converted into a string by passing it to str() to produce a user-friendly error message.
Using the try and except statements, you can handle errors more gracefully instead of letting the entire program crash.
"""
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('0', 20, 5,), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))
        