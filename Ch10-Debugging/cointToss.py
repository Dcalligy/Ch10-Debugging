import random

coin = ['heads', 'tails']
toss = str(random.choice(coin))
guess = input('Guess the coin toss! Enter heads or tails: ')

while guess not in coin:
    print('Incorect input...try again')
    guess = input('Guess the coin toss! Enter heads or tails: ')

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input('Guess the coin toss! Enter heads or tails: ')
    while guess not in coin:
        print('Incorect input...try again')
        guess = input('Guess the coin toss! Enter heads or tails: ')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game...')
