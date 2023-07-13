import random

def generate_number(min_num, max_num):
    return random.randint(min_num, max_num)

def play_game():
    min_num = 1
    max_num = 100
    attempts = 5
    target_number = generate_number(min_num, max_num)
    
    print("Welcome to Guess the Number!")
    print(f"I'm thinking of a number between {min_num} and {max_num}.")
    print(f"You have {attempts} attempts to guess the correct number.\n")
    
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        attempts -= 1
        
        if guess == target_number:
            print("\nCongratulations! You guessed the correct number!")
            break
        elif guess < target_number:
            print("Too low! Try again.\n")
        else:
            print("Too high! Try again.\n")
    
    if attempts == 0:
        print("\nGame over! You ran out of attempts.")
    
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("\nThank you for playing Guess the Number!")

# Start the game
play_game()
