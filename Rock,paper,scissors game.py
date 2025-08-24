# This line imports the built in Random function in Python, with which we can use to pick anything within a specific list or value
import random 

# This commands are here to count how many times someone won or drawed
user_wins = 0 
computer_wins = 0
draw = 0 

# This is the list from where the computer will pick randomly using the Random function
option = ["rock", "paper", "scissors"]

# We use the while loop so that we can end the program at an specific condition
while True:
    # We use the input() function so that the player can input a move
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower() # .lower() makes any input into lowercase letters
    # If the player entered q to quit the program will end using the break function
    if user_input == "q": 
        break
    
    # If the player did't choose rock, paper or scissors the program will send them back to the option menu by using the continue function 
    if user_input not in option:  
        print("Invalid input. Please try again.")
        continue    
    
    # The program will refer to the option varible and choose one of option (0 = rock, 1 = paper, 2 = scissors.)
    # Note: 0 is the starting index for a list in python and why we used a variable will make sense later
    # then the computer will choose randomly using the random function.  
    random_number = random.randint(0, 2)
    # This line creates a variable and refers to the variable option and the index value is THE VARIABLE random_number 
    computer_pick = option[random_number]
    # Shows what the computer picked
    print("Computer picked", computer_pick + ".")

    # All the 'if' and 'elif' conditions checks wether the player won.
    # The 'and' is a logical operator that checks wether both of the conditions are correct then does the operaion commanded to do
    if user_input == "rock" and computer_pick == "scissors":
        # Shows that the player won
        print("You won!")
        # Gives a point to the player
        user_wins += 1 
    
    # Same here but it uses 'elif' condition checks wether the player won.
    # Elif is used AFTER A 'if' CONDITION as a way to check something when the'if' codition didn't meet the coditions
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1     
    
    # Same way
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1   
    # Same way
    elif user_input == computer_pick: 
        print("It's a draw")
        draw += 1 
    #
    else:
        print("You lost!")
        computer_wins += 1    

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times. ") 
print("There were", draw, "draws!")
print("Goodbye!")

