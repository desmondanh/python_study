'''
Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place
is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
Say the number generated by the computer is 1038. An example interaction could look like this:
  Welcome to the Cows and Bulls Game! 
  Enter a number: 
  >>> 1234
  2 cows, 0 bulls
  >>> 1253
  1 cow, 1 bull
  ...
Until the user guesses the number.
'''

import random

def cow_bull(number, user_guess):
    cowbull = [0,0] #cows, then bulls count
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[0]+=1
        elif user_guess[i] in number:
            cowbull[1]+=1
    return cowbull

if __name__=="__main__":
    playing = True #gotta play the game
    number = str(random.randint(1000,9999)) #random 4 digit number
    guesses = 0
    duplicated = 0
    print("Let's play a game of Cowbull!") #explanation
    print("I will generate a four-digit number, and you have to guess the numbers.")
    print("For every number you guess right but in the wrong place, you get a bull. And for one in the right place, you get a cow.")
    print("The game ends when you get 4 cows!")
    for i in range(len(number)):
        if number[i] in number[i+1:4]:
            duplicated+=1
    if duplicated != 0:
        print(f'The number you have to guess has {duplicated} duplicate! Be aware!')
    print("Type exit at any time to exit.")
    # print(number)
    while playing:
        user_guess = input("Give me your best guess!\n")
        if user_guess in ['exit','Exit','EXIT']:
            print('Scared of a little game, what a coward! Hahaha')
            break
        cowbullcount = cow_bull(number,user_guess)
        guesses+=1

        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[0]==4:
            playing = False
            print("You win the game after " + str(guesses) + " guesses! The number was "+str(number))
            break #redundant exit
        else:
            print("Your guess isn't quite right, try again.")