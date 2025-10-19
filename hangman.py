###########################################################################################################################################
# Hangman Game Implementation
# By - Devish Kumar
# Date - 19 October 2025
# Version - 1.0
# This program allows a user to play the Hangman game in the console.
# The user has to guess a randomly selected word letter by letter within a limited number of attempts.

# Importing necessary modules
import random

# List of possible words for the Hangman game
Word_List = ['razzberry' , 'watermelon' , 'pineapple' , 'grapefruit' , 'pomegranate']

# Function to select a random word from the list
def get_random():
    word = random.choice(Word_List)
    return word

# Function to display the current state of the guessed word
def display_word(word, guessed_letters):
    display = ''
    for l in word:
        if l in guessed_letters:
            display += l + ' '
        else:
            display += '_ '
    return display.strip()

# Main function to run the Hangman Game 
def hangman():
    word = get_random()
    guessed_letters = set()
    attempts = 6 

    # Game Introduction 
    print('Welcome to Hangman Game!!')
    print('Rules :')
    print('1. You have to guess the word letter by letter.')
    print('2. You have 6 attempts to guess the word correctly.')
    print('Let\'s begin!\n')

    #Game Loop
    while attempts > 0: 

        # Display current state 
        print('Word : ' + display_word(word, guessed_letters))
        print('Guessed Letters : ' + ', '.join(sorted(guessed_letters)))

        # Display remaining attempts
        print('Attempts Remaining : ' + str(attempts))
        
        #Get user input
        g = input('Guess a letter : ').lower()

        # Process the guess

        # Check if letter has already been guessed
        if g in guessed_letters:
            print('You already guessed that letter. Try again.\n')
            continue

        # Check if guess is correct
        elif g in word:
            guessed_letters.add(g)
            print('Good guess!\n')

        # Check for invalid input   
        elif g.isalpha() == False or len(g) !=1:
            print('Invalid input. Please enter a single letter.\n')
            continue

        # Check if guess is incorrect
        elif g not in word:
            guessed_letters.add(g)
            attempts-=1
            print('Wrong Guess!\n')
        
        # Check if the word is completely guessed
        
        if all(l in guessed_letters for l in word):
            print('Congratulations! You guessed the word: ' + word)
            break

    # End of Game iF attempts run out
    else:
        print('Sorry, you ran out of attempts. The word was: ' + word)

# Start the Hangman game
if __name__ == '__main__':
    hangman()

#End of hangman.py
## Enjoy playing Hangman!
###########################################################################################################################################