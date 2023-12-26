#Purna Chhetri
#CPT-101 Lab 13 Part 2
#This program counts how many vowels and consonant in a string

#Main function
def main():
    #Input/introduction
    print("This program will count how many vowels and consonants are in a word or sentence")
    sentence = input("Please enter a word or sentence: ")

    #Function calls
    vowel_total, consonant_total = vowel_counter(sentence)

    #Results output
    print(f"That phrase had {vowel_total} vowels and {consonant_total} consonants")

#This method counts the vowels and consonant from the string passed in
def vowel_counter(word):
    #Creating a list of all the vowels
    vowels = ["a","A","e","E","i","I","o","O","u","U"]
    #Counter variables
    vowel_count = 0 
    consonant_count = 0
    vowel_check = False
    #Counting vowels and consonants
    for char in word:
        if char.isalpha():
            for count in range(len(vowels)):
                if char == vowels[count]:
                    vowel_check = True
            if vowel_check == True:
                vowel_count += 1
            elif vowel_check == False:
                consonant_count += 1
            vowel_check = False
    #Returning total
    return vowel_count, consonant_count
#Running main
main()