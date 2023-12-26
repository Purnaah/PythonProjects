#Purna Chhetri
#CPT-101 Lab 10 Part 2
#This program stimulates a dice rolling game

import random
#Main function
def main():
    #Variables
    dice_sided = None
    total = 0
    #Introduction 
    print("Welcome to my dragon dice program")
    
    #While loop for continuing until 0 is entered 
    while dice_sided != 0:
        #Input from user
        dice_sided = int(input("Which die would you like to roll(d4,d6,d8,d10,d12,d20)? "))
        if dice_sided == 0:
            print("Thanks for using my dragon dice program")
        else:
            #Input validation 
            while dice_sided != 4 and dice_sided != 6 and dice_sided != 8 and dice_sided != 10 \
            and dice_sided != 12 and dice_sided != 20:
                print("Invalid response please try a different value")
                dice_sided = int(input("Which die would you like to roll(d4,d6,d8,d10,d12,d20)? "))
            roll_amount = int(input(f'How many d{dice_sided}s would you like to roll? '))

            #Looping the dice roll
            print("You rolled:",end=" ")
            for x in range(0,roll_amount):
                if x != roll_amount-1:
                    dice_value = roll(dice_sided)
                    print(dice_value,end=",")
                    total+=dice_value
                else:
                    dice_value = roll(dice_sided)
                    print(dice_value)
                    total+=dice_value
            print(f'Your total is {total}')
#This function genrates a random value for the dice     
def roll(die_type):
    roll_value = random.randint(1,die_type)
    return roll_value
#Running main function
main()