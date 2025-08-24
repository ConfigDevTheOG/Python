import random  # Import the built-in random module

# Score counters
user_wins = 0
computer_wins = 0
draws = 0

# Possible moves
options = ["rock", "paper", "scissors"]

# Game loop
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()  # Convert input to lowercase
    
    # Quit condition
    if user_input == "q":
        break
    
    # Validate input
    if user_input not in options:
        print("Invalid input. Please try again.")
        continue    
    
    # Computer randomly picks a move
    computer_pick = random.choice(options)
    print("Computer picked", computer_pick + ".")
    
    # Check outcomes
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a draw.")
        draws += 1
    else:
        print("You lost!")
        computer_wins += 1

# Final score summary
print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")
print(f"There were {draws} draws.")

# I hope this helped you. Good luck on your journey, my programmer friend. See you again...
#
# P.S. If you get hired by a company one day, remember that I helped you! 
# Maybe we’ll meet again if you follow me. :)
