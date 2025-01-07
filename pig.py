# Sam Matiishin
# Pig Project Program
# Description: User will play Pig dice game against computer and if there
# is a winner, it will be announced at the end

import random

# Secondary function called by the main function that handles the CPU turn and returns a total
def computer_turn_score():
    # Initialize variable for the CPU round total
    cpu_total = 0
    # Initialize variable for the string output
    rolls = ""
    # Initialize variable for the index of each letter in the string output
    index = 0
    # Initialize list that keeps track of all CPU rolls in the turn
    cpu = []
    # Initialize variable that limits the CPU total
    CPU_CAP = 20

    # Loop that runs until the round total is either greater than 20 or if the CPU
    # rolls a 1, both submitting a corresponding round total
    while int(cpu_total) < CPU_CAP:
        
        # Initialize variable roll to be equal to the value obtained from the die roll
        roll = die_roll()
        # Add each roll to the list
        cpu.append(roll)
        print("\n")
        
        # Boolean statement that returns a total of 0 if the CPU rolls a 1
        if roll == 1:
            cpu_total = 0
            
            # Remove 1 from the list and replace it with the string "turn ends"
            cpu.remove(int(1))
            cpu.append('turn ends')
            
            # The rolls variable converts each value in the list into a single string
            for number in cpu:
                rolls += (str(number)+",")
                
            # Display each roll during the turn and remove the last comma
            print("\nThe computer rolls: ")
            while index < len(rolls) - 1:
                print(rolls[index], end = "")
                index += 1
            print("\t\t (Points this round: "+str(cpu_total)+")")
            
            # Return the cpu total for the round back to the main function
            return cpu_total
        else:
            # Each roll is added to the total
            cpu_total += int(roll)

    # Loop that converts each value in the list into a single string
    for number in cpu:
        rolls += (str(number)+",")

    # Display each roll during the turn and remove the last comma
    print("The computer rolled: ")
    while index < len(rolls) - 1:
        print(rolls[index], end = "")
        index += 1
    print("\t\t (Points this round: "+str(cpu_total)+")")

    # Return the cpu total for the round back to the main function
    return cpu_total

# Secondary function called by the main function handles the user turn and returns
# a total back to the main function
def user_turn_score():
    # Initialize variable for user round total
    total = 0
    # Initialzie variable for the string output
    rolls = ""
    # Initialize variable for the index of each letter in the string output
    index = 0
    # Initialize list that keeps track of all user rolls in the turn
    player = []

    # Loop that runs until the user chooses not to continue or if the user
    # rolls a 1, both submitting a corresponding round total
    while roll_or_end() == "YES":

        # Initialize variable roll to be equal to the value obtained from the die roll 
        roll = die_roll()
        
        print("You rolled "+str(roll))

        # Add each roll to the list
        player.append(roll)

        # Boolean statement that returns a total of 0 if the user rolls a 1
        if roll == 1:
            total = 0

            # Remove 1 from the list and replace it with the string "turn ends"
            player.remove(int(1))
            player.append(str('turn ends'))

            # The rolls variable converts each value in the list into a single string
            for number in player:
                rolls += (str(number)+",")

            # Display each roll during the turn and remove the last comma
            print("\nThe user rolls: ")
            while index < len(rolls) - 1:
                print(rolls[index], end = "")
                index += 1
            print("\t\t (Points this round: "+str(total)+")")

            # Return the round total back to the main function
            return total
        else:
            # Each roll is added to the total
            total += int(roll)
    # Add stop to the list to indicate that the user chose to end their turn
    player.append("stop")
    # The rolls variable converts each value in the list into a single string
    for number in player:
        rolls += (str(number)+",")
        
    # Display each roll during the turn and remove the last comma
    print("The user rolled: ")
    while index < len(rolls) - 1:
        print(rolls[index], end = "")
        index += 1
    print("\t\t (Points this round: "+str(total)+")")

    # Return the round total back to the main function
    return total

# Secondary function called by another secondary function that obtains a user input to determine whether a user
# wants to continue rolling or exit
def roll_or_end():
    user_choice = input("Type 'Yes' to roll or press any other key to end your turn:")
    print("\n")

    # Return the user input in capital letters to be evaluated in another function
    return user_choice.upper()

# Secondary function called by other secondary functions that returns a value between 1 and 6
# to represent a die
def die_roll():
    roll = random.randint(1,6)
    return roll

# Secondary function called by the main function that evaluates overall totals and determines
# if there is a winner
def check_for_win(score):
    # Initialize variable for the winning score total
    WINNING_SCORE = 100
    # Boolean statement that returns true if greater than or equal to 100
    if score >= WINNING_SCORE:
        return True
    return False

# Primary function that executes the program
def main():
    # Initialize boolean variable that determines if the game should be continued
    continue_game = True
    # Initialize boolean variable that alternates turns between the user and the CPU
    change_turn = False
    # Initialize variable for user overall total
    user_total = 0
    # Initialize variable for CPU overall total
    cpu_total = 0

    # Welcome the user, and offer instructions if confused, otherwise start the program
    print("Welcome to this program!",'\n'+"You will be playing Pig against a computer."'\n'+"Lets see if you can win!")
    user_option = input("\nType 'help' to view instructions, or press ENTER to begin:")
    if user_option.upper() == "HELP":
        print("\nPig is a game that has two players that alternate turns rolling dice.\nIn our case, there will be one human player and one computer player.\nEach player’s goal is to get 100 points rolled on a normal six-sided die first.\nEach turn consists of the rolling the die repeatedly until\nyou decide to stop or until you roll a 1.\n\n") 

    # Loop that runs until a winner is determined, displaying who won and the final scores
    while continue_game == True:

        # Boolean statement that runs during the user turn
        if change_turn == False:

            # Add the user round total to the user overall total and display current totals
            user_total += user_turn_score()
            print("Current totals:\t\tPlayer:",user_total,"CPU:",str(cpu_total))

            # Boolean statement that determines if the user has at least 100 points, and displaying victory if true
            if check_for_win(user_total) == True:
                print("You have won with",user_total,"points!\nGame over!")
                continue_game = False

            # Switch the turn to the CPU
            change_turn = True

        # Boolean statement that runs during the CPU turn
        elif change_turn == True:

            # Add the CPU round total to the CPU overall total and display current totals
            cpu_total += computer_turn_score()
            print("Current totals:\t\tPlayer:",user_total,"CPU:",str(cpu_total))

            # Boolean statement that determines if the CPU has at least 100 points, and displays victory if true
            if check_for_win(cpu_total) == True:
                print("Too Bad. The CPU won with",cpu_total,"points.\nGame Over!")
                continue_game = False

            # Switch the turn to the user
            change_turn = False

# Command that executes the main function
main()
