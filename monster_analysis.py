#Purna Chhetri
#CPT-101 Final Project
#This program does an analysis of the monster encounter and finds the character that wins the most after 200 battles

#Importing random module 
import random
#Importing math module
import math
#Main function
def main():
    #Introduction
    print("This program will simulate 200 battles with each of the classes from Monster Hunter 2")
    #Character pick and stats
    win_counter = [0]*4 #A list of 4 to count each class's wins
    flag = True #boolean variable for loop
    win_duplicate = 0 #counter for multiple winners
    #Initiating the game
    for class_number in range(1,5): #Looping for each class
        for count in range(1,201):#Iterating 200 times
            #Generating player and monster
            class_name,player_health,max_damage,hit_chance = player_generator(class_number) 
            monster_health = 36
            #resetting boolean for each iteration
            flag = True
            while flag==True: #iterates until someone wins
                player_damage = user_turn_damage(max_damage)
                if monster_dodge() == True:
                    dodged_damage = player_damage*0.4
                    player_damage-=dodged_damage
                    player_damage = math.floor(player_damage)
                    monster_health-=player_damage
                else:
                    monster_health-=player_damage
                monster_damage = computer_turn_damage()
                if hit_check(hit_chance) == False:
                    player_health+=0
                else:       
                    player_health-=monster_damage
        
                if check_for_winner(player_health,monster_health) == True:
                    if monster_health <= 0:
                        #Ending round and adding to win counter
                        flag = False 
                        win_counter[class_number-1] +=1
                    else:
                        flag = False
    #Results
    print("Here are the results: ") 
    for count in range(0,4): #displaying results for each class
        name_class,_,_,_ = player_generator(count+1)
        print(f"{name_class}: {win_counter[count]} wins")
    #Finding the class with most wins
    most_wins = max(win_counter) 
    class_wins = win_counter.index(most_wins)
    winner_class_name,_,_,_ = player_generator(class_wins+1) #getting the name of the class

    #Displaying the class with the most wins
    for count in range(1,5): #in case there are multiple classes with the most wins
        if win_counter[count-1] == most_wins:
            win_duplicate+=1
    if win_duplicate>1:
        print("There were multiple classes with the most amount of wins")
        for count in range(1,5):
            if win_counter[count-1] == most_wins:
                winner_class_name,_,_,_ = player_generator(count)
                print(f'The {winner_class_name} class had {most_wins} wins')
    else:
         print(f'The class with the most wins was {winner_class_name} with {most_wins} wins')
    #Goodbye message
    print("Thanks for using my program!")
    
#This function generators the player's character and its stats
def player_generator(number):
    #Assigning stats based on passed in number
    player_choice = number
    if player_choice == 1:
        class_name = "Knight"
        player_health = 24
        max_damage = 10
        chance_hit = 70
    elif player_choice == 2:
        class_name = "Mage"
        player_health = 18
        max_damage = 16
        chance_hit = 60
    elif player_choice == 3:
        class_name = "Rogue"
        player_health = 18
        max_damage = 12
        chance_hit = 50
    elif player_choice == 4:
        class_name = "Tinkerer"
        player_health = 16
        max_damage = 20
        chance_hit = 65
    #Returning stats for chosen class
    return class_name, player_health,max_damage,chance_hit

#This function returns the monsters damage, with the highest being 6
def computer_turn_damage():
    damage = random.randint(1,6)
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
    if monster_health <= 0:
       return True 
    elif player_health <= 0:
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
