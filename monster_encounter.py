#Purna Chhetri
#CPT-101 Final Project
#This program simulates a monster encounter

#Importing random module 
import random
#Importing math module
import math
#Main function
def main():
    #Introduction
    print("Welcome to Monster Hunter 2")
    
    #Variables
    round = 1
    monster_health = 36
    total_monster_health = 36
    #Character pick and stats
    class_name,player_health,max_damage,hit_chance = player_generator()
    total_health_player = player_health
    #Game introduction
    print("You have taken on a quest to find the philosophers stone, a mystical stone that is said to grant immortality to whoever finds it. While journeying through")
    print("The Devils Way, an infamous forest that is rumored to be possessed by a powerful demom, you hear omnious sounds.")
    print("You suddenly start to feel a powerful aura and before you know it, you hear a laugh that can only be described as devilish.")
    print(f'Your {class_name} comes face to face with Abaddon, a powerful demon.')

    #Initiating the game
    while check_for_winner(player_health,monster_health)==False:
        start_round = int(input("Enter 1 to start round: ")) #Prompting user to type 1 to start the round, gives them a chance to see how the battle progresses
        print(50*"-") #for better visibility 
        if start_round == 1: 
            print(f'Round {round}:') #Displaying current round
            #Player turn damage
            player_damage = user_turn_damage(max_damage) 
            #Checking if the monster dodged some of the damage
            if monster_dodge() == True:
                dodged_damage = player_damage*0.4 #reduced damage if monster dodges
                player_damage-=dodged_damage
                player_damage = math.ceil(player_damage) #rounding down
                #Displaying dodged damage
                print("The monster dodged 40 percent of your damage")
                print(f'Your {class_name} hit Abaddon for {player_damage} points of damage')
                monster_health-=player_damage #reducing monster health by the damage done
            else: #deals regular damage if it's not dodged
                print(f'Your {class_name} hit Abaddon for {player_damage} points of damage') 
                monster_health-=player_damage 
            #Monster turn damage
            monster_damage = computer_turn_damage()
            #Checking if player dodged the monster's attack
            if hit_check(hit_chance) == False:
                print("Abaddon missed his attack this turn") #no damage is done if attack is dodged
                print(50*"-")
            else:
                print(f"Abaddon hits your {class_name} for {monster_damage} points of damage")
                print(50*"-")
                player_health-=monster_damage 
            #Displaying the results of the round
            if player_health <= 0: #making sure negative health is not shown
                print("Results: ")
                print(f"{class_name} health's- 0/{total_health_player}, Abaddon's health - {monster_health}/{total_monster_health}")
                print(50*"-")
            elif monster_health <= 0:
                print("Results: ")
                print(f"{class_name}'s health - {player_health}/{total_health_player}, Abaddon's health - 0/{total_monster_health}")
                print(50*"-")
            else: 
                print("Results: ")
                print(f"{class_name}'s health - {player_health}/{total_health_player}, Abaddon's health - {monster_health}/{total_monster_health}")
                print(50*"-")
            round+=1
        else: #if the user enters anything other than 1 
            print("Invalid response, please try again")

        #Checking if there was a winner 
        if check_for_winner(player_health,monster_health) == True:
            if monster_health <= 0: #if monster health is zero or lower
                print(f"Your {class_name} has won the fight! Congrats!")
            else: #if player health is zero or lower
                print(f"Your {class_name} was defeated")
    #Goodbye message
    print("Thank you for playing Monster Hunter 2, we hope you enjoyed it!")
            
#This function generators the player's character and its stats depending on the user's choice
def player_generator():
    #Using boolean for input validation
    flag = True
    while flag == True:
        #Displaying choice menu
        print("1. Knight 2. Mage 3. Rogue 4. Tinkerer")
        player_choice  = int(input("Choose your character's class(1, 2, 3, or 4): ")) 
        
        #Assigning class stats to variable based on choice
        if player_choice == 1:
            class_name = "Knight"
            player_health = 24
            max_damage = 10
            chance_hit = 70
            flag = False
        elif player_choice == 2:
            class_name = "Mage"
            player_health = 18
            max_damage = 16
            chance_hit = 60
            flag = False
        elif player_choice == 3:
            class_name = "Rogue"
            player_health = 18
            max_damage = 12
            chance_hit = 50
            flag = False
        elif player_choice == 4:
            class_name = "Tinkerer"
            player_health = 16
            max_damage = 20
            chance_hit = 65
            flag = False
        else:
            print("Invalid choice, please try again")
    #Returning class variables
    return class_name, player_health,max_damage,chance_hit

#This function returns the monsters damage, with the highest being 6
def computer_turn_damage():
    damage = die_roll(6)
    return damage
#This function returns the players damage, with the passed value being the maximum
def user_turn_damage(num): 
    damage = die_roll(num)
    return damage
#This function returns a random number, with the passed value being the maximum 
def die_roll(number):
    random_damage = random.randint(1,number)
    return random_damage
#This function generates a random number between 1 and 100, returns true if its less than the passed in value, false if its greater
def hit_check(num):
    random_num = random.randint(1,100)
    if random_num<=num:
        return True
    else:
        return False
#This function takes in two values and checks if its less than or equal to zero, returning true if any of them is zero or less
def check_for_winner(player_health,monster_health):
    if monster_health <= 0 or player_health <= 0:
       return True 
    else:
        return False
#This function does the same thing as hit_check(num), but without a value passed in 
def monster_dodge():
    percentage_hit = random.randint(1,100)
    if percentage_hit <= 85:
        return False
    else: 
        return True
#Running main
main()