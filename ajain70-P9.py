#P9: Using Regular Expressions
#DATE: 7th November 2022
#@author: Atishay Jain
#Question: Write a script that finds all of the capitalized words (not words in all caps except individual letters) in a text file and presents them in alphabetical order.
import re #importing regular expression library
file = input("Enter the file name with its extension: ")
f = open(file, 'r') #opening the file in read only mode.
try: #try if the file name entered is valid or not.
    #iterating through every line of the file.
    for line in f: 
        line = line.rstrip() #stripping unwanted whitespaces from it.
        #print(line)
        x = re.findall('[A-Z].\S*', line) #file all words that start with A to Z and .\S* denotes that print everything in that word also and not just the first characters. 
        try: #try if any capitalized word exist in the lines of the file.
            if len(x) > 0: #if any capitalized words exist then print them in same line.
                print(x, end = " ")        
        except:
            print("Sorry. No capitalized words were found in this file.") #handle a case where no capitalized words are present.
except:
    print('The file name entered in invalid or does not exist.') #handle a case where the file name entered is invalid.