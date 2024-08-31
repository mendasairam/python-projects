import time

def intro():
    """Introduction to the game."""
    print("Welcome to the Choose Your Own Adventure game!")
    time.sleep(1)
    print("You find yourself at the entrance of a mysterious forest.")

def choose_path():
    """First choice: Enter the forest or walk away."""
    print("\nDo you want to enter the forest or walk away?")
    print("1. Enter the forest")
    print("2. Walk away")
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        forest_path()
    elif choice == "2":
        walk_away()
    else:
        print("\nInvalid choice. Please try again.")
        choose_path()

def forest_path():
    """Second choice: Choose between cave or clearing."""
    print("\nYou step into the forest and see two paths.")
    print("One path leads to a dark cave, and the other leads to a sunny clearing.")
    print("Which path do you choose?")
    print("1. Go to the cave")
    print("2. Go to the clearing")
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        cave_path()
    elif choice == "2":
        clearing_path()
    else:
        print("\nInvalid choice. Please try again.")
        forest_path()

def cave_path():
    """Third choice: Open the chest or leave it alone."""
    print("\nYou enter the cave and find a treasure chest.")
    print("Do you want to open the chest or leave it alone?")
    print("1. Open the chest")
    print("2. Leave it alone")
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        print("\nYou open the chest and find a pile of gold coins. Congratulations, you are rich!")
    elif choice == "2":
        print("\nYou decide to leave the chest alone and exit the cave. Maybe another adventurer will find it.")
    else:
        print("\nInvalid choice. You wander aimlessly in the cave.")
    
    end_game()

def clearing_path():
    """Third choice: Drink from the fountain or enjoy the view."""
    print("\nYou walk into the clearing and find a beautiful meadow with a magical fountain.")
    print("Do you want to drink from the fountain or sit and enjoy the view?")
    print("1. Drink from the fountain")
    print("2. Sit and enjoy the view")
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        print("\nThe water from the fountain grants you eternal youth. You feel rejuvenated and happy!")
    elif choice == "2":
        print("\nYou sit and enjoy the serene view. It's a peaceful moment in your adventure.")
    else:
        print("\nInvalid choice. You decide to head back to the forest entrance.")
    
    end_game()

def walk_away():
    """Option for walking away from the forest."""
    print("\nYou decide to walk away from the forest and return home. Sometimes it's best to avoid danger.")
    end_game()

def end_game():
    """End the game and prompt to play again."""
    print("\nThank you for playing! Would you like to play again?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter the number of your choice: ")
    
    if choice == "1":
        start_game()
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid choice. Exiting the game.")
        print("Goodbye!")

def start_game():
    """Start or restart the game."""
    intro()
    choose_path()


if __name__ == "__main__":
    start_game()
