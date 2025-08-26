import random

def number_guesser():
    numberGuess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guesser!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed:
        try:
            userGuess = int(input("Enter your guess: "))
            attempts += 1

            if userGuess < numberGuess:
                print("Too low! Try again.")
            elif userGuess > numberGuess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")
    
number_guesser()