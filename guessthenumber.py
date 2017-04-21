# -*- coding: utf-8 -*-

"""
Igra ugani skrito število
Avtor: Tjaša K. Petrič

Računalnik bo naključno izbral število.
Poskusi so omejeni na 4, nato napiše skrito število.
"""

# -*- coding: utf-8 -*-

"""
Igra ugani skrito število, posodobljena
Avtor: Tjaša K. Petrič

Računalnik bo izbral naključno število.
Poskusi so omejeni na 4, nato napiše skrito število.
"""

import random

def start():
    hidden_number = random.randint(10, 90)
    attempts = 1
    print "Let's play a game! Can you guess the hidden number?"

    while True:
        guessed_number = int(raw_input("Enter any number between 10 and 90: "))

        if guessed_number == hidden_number:
            print "CONGRATULATIONS! You got it! The hidden number is " + str(hidden_number) + " !"
            print "It took you " + str(attempts) + " attempts."
            again = raw_input("Would you like to play again? Type Y to play again or N to exit the game:").lower()
            if again == "y":
                print "Let's play again!"
            elif again == "n":
                print "Hope to see you again!"
                break

        if guessed_number > hidden_number:
            print "NOPE! Sorry. The hidden number is lower than " + str(guessed_number) + "!"
        elif guessed_number < hidden_number:
            print "WRONG! Sorry. The hidden number is higher than " + str(guessed_number) + "!"
            attempts += 1

        if attempts == 5:
            print "Sorry, you have reached the maximum number of attempts!"
            print "The hidden number was " + str(hidden_number) + "."
            break

if __name__  == "__main__":
    start()
    print "Game over."
