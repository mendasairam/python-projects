import random

def number_guessing_game():
    
    print("Welcome to the Number Guessing Game!")
    
   
    lower_bound = 1
    upper_bound = 100
    
   
    number_to_guess = random.randint(lower_bound, upper_bound)
    
    attempts = 0
    max_attempts = 10 
    
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            
            if guess < lower_bound or guess > upper_bound:
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
                continue
            
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if guess != number_to_guess:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

number_guessing_game()
