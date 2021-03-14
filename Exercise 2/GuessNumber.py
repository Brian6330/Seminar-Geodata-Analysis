import random
# GuessNumber.py asks for a random number between 0 and 100.
# As long as the random number is not reached, the script keeps on going.

# Returns a random integer in range [0, 100], including both end points
random_number = random.randint(0, 100)

# Asks for a random number; only accepts numbers as input
guessed_number = input('''Welcome!
Can you guess what number between 0 and 100 I'm thinking of?
Please enter your guess: ''')


while True:
    guess = int(input("Enter guess (between 0 and 100): "))
    if guess < random_number:
        print("Try higher.")
    elif guess > random_number:
        print("Try lower.")
    elif guess == random_number:
        print("You found it!")
        break
