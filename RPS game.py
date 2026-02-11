import random

def play_game():
    # Initialize scores
    user_score = 0
    computer_score = 0
    
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.")
    
    while True:
        # User Input
        user_choice = input("\nEnter your choice (rock, paper, scissors): ")
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Computer Selection
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Game Logic
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "scissors" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "rock")
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Display Current Scores
        print(f"Scores -> You: {user_score}, Computer: {computer_score}")
        
        # Play Again
        play_again = input("\nDo you want to play another round? (yes/no): ")
        if play_again != "yes":
            print("\nThanks for playing!")
            print(f"Final Scores -> You: {user_score}, Computer: {computer_score}")
            if user_score > computer_score:
                print("You are the overall winner!")
            elif user_score < computer_score:
                print("Computer is the overall winner!") 
            else:
                print("It's an overall tie!")
            break

# Run the game
play_game()


