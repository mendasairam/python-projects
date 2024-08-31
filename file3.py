import random

def get_computer_choice():
    
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
  
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def play_game():
 
    print("Welcome to Rock-Paper-Scissors!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "draw":
        print("It's a draw!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def main():

    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    
    print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()
