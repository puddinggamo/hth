import random 
# Guessing game Candy, Deney, Alicia, Josue, Christian, KJ


def generate_random_number():
    random_number = random.randint(1,100)
    return random_number 

def get_user_guess():
    while True:
        try: 
            guess_str = input("Enter your guess (1-100): ")
            guess = int(guess_str)

            if 1 <= guess <= 100: # allows user to get numbers spanning 1 to 100
                return guess
            else:
                print("Invalid input. Please Enter number within the range.")
        except ValueError:
            print("Invalid input. Please enter an integer.") # Tells whether the number inputted is incorrect or not included.
def play_guessing_game():
   secret_number = generate_random_number()
   attempts = 0
   guessed_correctly = False 
# sets up a way to show both attempts as well if the number is correct or not
   print("Welcome to the Number Guessing Game!")
   print("I have chosen a number between 1 and 100.") # just dialogue basically

   while not guessed_correctly:
        attempts = 1
        user_guessed = get_user_guess()

        if user_guessed < secret_number:
            print("Too low Try again.")
        elif user_guessed > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts")
            guessed_correctly = True 

        # indicates whether the user has gotten the guess correct or not. Telling them the problem with their guess.

if __name__ == "__main__":
    play_guessing_game()
def game_loop():  # looping the game so it coud be played all over again. 
    while True:
        print("\n--- Starting a new round of the guessing game ---")
        print("You guessed the correct number!")

        play_again = input("Do you want to play again? (Yes/No):") # giving the option whether to play again or not.
        if play_again != 'yes':
            print("Thanks for playing!")
            break
    # Finishing the game and resetting progress. Exiting. 

if __name__ == "__main__": 
    game_loop()