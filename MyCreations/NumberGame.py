# This is a guess the number game

import random

print('Hello. What is your name?')
name = input()

print('Alright, ' + name + ', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)

# print('DEBUG: The number is ' + str(secretNumber) + '.')

for guessesTaken in range(1, 7):
    #code here
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
        guessesTaken = guessesTaken + 1
    elif guess > secretNumber:
        print('Your guess is too high.')
        guessesTaken = guessesTaken + 1
    else:
        break # this is the correct guess

if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Nope. My number was ' + str(secretNumber) + '.')
    
    


