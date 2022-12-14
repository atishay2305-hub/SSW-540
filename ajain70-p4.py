'''
Subject : SSW-540 Fundamentals of Software Engineering
Program/HW-04/P4
Date: 3rd October 2022
Author's Name: Atishay Jain
 
Question: Guess a Number using loops and a function.

'''

import random
answer = 0 #variable that helps in returning values 0,1,-1 based on the number the user guesses.

def guessing(): 
    name = input("Hello! What is your name?") #taking the name as an input in the "name" variable
    guesses = 0 #this is a variable that is acting as a count variable which is initialized to 0 as it has count being equal to 0.
    number_guessed = 0 #this is the number that user will guess and will it be stored in the variable called "number_guessed"
    num_to_be_guessed = random.randint(1,20) #this is the random integer number between 1 and 20 that will be the actual number that user needs to guess.
    print(f"Well, {name}, I am thinkin of a number between 1 and 20") 
    while number_guessed != num_to_be_guessed:
        try:    #try taking input and try if the number guessed is equal to number to be guessed or not
            number_guessed = int(input("Take a guess."))
            guesses +=1
            if guesses > 6:
                print(f"the number I was thinking of was {num_to_be_guessed}")
                break
            else:
                if number_guessed == num_to_be_guessed:
                    print(f"Good job, {name}! You guessed my number in {guesses} guesses")
                    answer = 0
                if num_to_be_guessed < number_guessed and number_guessed < 20:
                    print("Your guess is too high.")
                    answer = -1
                elif number_guessed < num_to_be_guessed and number_guessed > 0:
                    print("Your guess is too low.")
                    answer = 1
                else:
                    print("Please enter a value in the range only.")
        except: #exception is that if user enters any value apart from a integer. for example: if user enters "a" as input
            print("Please enter a valid input")
#returning outputs for users
    if answer == 0:
        return 0 #when number_guessed == num_to_be_guessed
    elif answer == -1:
        return -1 #when num_to_be_guessed < number_guessed:
    else:
        return 1 #when num_to_be_guessed > number_guessed:

if __name__ == "__main__":
    guessing() #calling the function inside the main function