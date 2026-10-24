import random # Imports
import sys
import time

points = 0 # Assign variables
guesses = 3

print('Welcome to the random number generator') # Introduction
print('The number is between 1 and 100 and changes every time')
print('You have 3 guesses')
print('1st guess = 10 points')
print('2nd guess = 5 points')
print('3rd guess = 3 points')

#               ---Main code---

while True:
    rng = random.randint(1, 100)  # Set up the random number
    #print(rng) #ERROR CHECK LINE

    while True: # Process the guess
        while True:  # Check guess is within rules
            try:
                guess = int(input('Guess a number between 1 and 100: '))
                if guess < 101 and guess > 0:
                    break
                else:
                    print('Invalid choice')
            except ValueError:
                print('Invalid')

        if guess != rng:
                guesses = guesses - 1
                print(f'Incorrect guess, {guesses} guesses left')

                if guesses == 0:
                    print('Your out of guesses')
                    print(f'The number was {rng}')
                    break

        elif guess == rng:
            print('You guessed right')
            break

        else:
            break

#               ---Points area---

    if rng == guess and guesses == 3: # 1st guess
        print('You get 10 points!')
        points += 10 # Assign points
        print(f'Your total amount of points is {points}')

    elif rng == guess and guesses == 2: # 2nd guess
        print('You get 5 points!')
        points += 5 # Assign points
        print(f'Your total amount of points is {points}')

    elif rng == guess and guesses == 1: # 3rd guess
        print('You get 3 points!')
        points += 3 # Assign points
        print(f'Your total amount of points is {points}')

    else:
        print('Better luck next go')

#               ---Play again?---

    while True:
        print('Would you like to play again?')
        again = input('Y/N: ')
        if again.lower() == 'n':
            print('Thanks for playing')
            time.sleep(2) # Allows player to read goodbye message
            sys.exit()

        elif again.lower() == 'y':
            guesses = 3 # Set guesses up for next play
            break

        else:
            print('Invalid input')
