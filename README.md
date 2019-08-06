# Python Debugging
Chapter 10 examples from the book Automate the Boring Stuff with Python. Topics covered in this chapter include:
* Raising Exceptions
* Getting the Traceback as a string
* Assertions
* Logging and Logging Levels
* Using the Debugger

## Debugging Coin Toss
For practice, write a program that does that following.

The following program is meant to be a simple coin toss guessing game. The player gets two guesses (it's and easy game). However, the program has several bugs that keep the program from working correctly.

```
import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails: ')
    guess = input()
toss = random.randint(0, 1) # 0 is for tails, 1 is for heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game...')
```
