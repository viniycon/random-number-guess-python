import random
import time

win = 0

while True:
    print('Select a dificulty, easy (1-10), medium (1-20), hard (1-50)')
    while True:
        try:
            mode = int(input('Easy = 1, Medium = 2, Hard = 3:   '))
            if mode == 1:
                difi = 10
                maxguess = 8
                break
            elif mode == 2:
                difi = 20
                maxguess = 7
                break
            elif mode == 3:
                difi = 50
                maxguess = 6
                break
            else:
                print('Invalid option')
        except ValueError:
            print('Numbers only')

    num = random.randint(1,difi)
    while True:
        try:
            guess = int(input(f'Guess a number 1-{difi}:   '))
            break
        except ValueError:
            print('Numbers only')
    numguess = 1
    print(f'You have {maxguess - numguess} guesses left')

    while guess != num:
        numguess +=1

        if guess > num:
            print('Guess lower')
        elif guess < num:
            print('Guess higher')

        while True:
            try:
                guess = int(input(f'Guess a number 1-{difi}:   '))
                break
            except ValueError:
                print('Numbers only')
        if guess != num:
            print(f'You have {maxguess - numguess} guesses left')

        if numguess >= maxguess:
            print('Out of guesses, the number was', num)
            break

    if guess == num:
        print('It took you', numguess, 'guesses')
        win +=1

    again = input('Do you want to play again? (Y/N): ').lower()
    if again == 'n':
        print('Thanks for playing!')
        print('You won', win, 'time(s)')
        time.sleep(2.5)
        break
