import random
# GuessNumber.py asks for a random number between 0 and 100.
# As long as the random number is not reached, the script keeps on going.

# Returns a random integer in range [0, 100], including both end points
random_number = random.randint(0, 100)

# Asks for a random number; only accepts numbers as input
guessed_number = input('''Welcome!
Can you guess what number between 0 and 100 I'm thinking of?
Please enter your guess: ''')


while int(guessed_number) != random_number:
    if int(guessed_number) < random_number:
        guessed_number = input('''
        Your number was smaller than mine!
        Please try again: ''')
    elif int(guessed_number) > random_number:
        guessed_number = input('''
        Your number was larger than mine!
        Please try again: ''')
