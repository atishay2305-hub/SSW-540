from socket import J1939_MAX_UNICAST_ADDR
from unittest import FunctionTestCase


P3: User defined functions
Author: Atishay Jain
Date: 25/09/2022

#program to return the maximum of three numbers

def maxOfThree(): #user-defined function
    try: #taking input from user for values a,b,c
        a = int(input("Enter first value")) 
        b = int(input("Enter second value"))
        c = int(input("Enter third value"))
        maximum = 0 #defining a variable named "maximum" which is initialized to 0

        if (a > b) and (a > c):
            maximum = a #assigning value of "a" to "maximum"
        elif (a < b) and (c < b):
            maximum = b #assigning value of "b" to "maximum"
        else:
            maximum  = c #assigning value of "c" to "maximum"
        print("The Maximum of {} {} {} is {}". format(a,b,c, maximum)) #here maximum will return the maximum number between a,b,c
    except:
        print("Wrong Input") #if any other value is entered by the other such as a string value then it returns "Wrong Input"

if __name__ == "__main__": #main function
    maxOfThree() #calling the function  "maxofThree()"