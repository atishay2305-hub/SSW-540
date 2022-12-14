#P7: Finding and counting unique items
#Date: 24th October 2022
#Author: Atishay Jain

from nbformat import read

file_name = input('Enter the file name: ') #user input for the file name 
#user enters the file : 'mbox.txt'
d = dict() #initializing a dictionary that will take the input from the file
Total_mails = 0 #total number of mails that are in the file

try:
    file = open(file_name, 'r') #file is a variable that will store the file name and open the file in read only mode
    for i in file: #i is the iterator in file variable
        i = i.rstrip() #this will reduce all the whitespaces
        if i.startswith('from:'): 
            continue #if from: does not exist in the keys then continue
        print(i) #printing each element in the file that has from: in the starting
        d.update(file[:20]) #updating the dictionary with all the keys that has from: <senderMail>
        Total_mails = Total_mails + 1 #incrementing the total number of mails
        print(Total_mails) #printing the total mails

    print(d.items) 
    rev_dict = {} #second dictionary for copying the unique items in initial dictionary
    for key, value in d.items():
        rev_dict.setdefault(value, set()).add(key)
        count = count + 1 #unique item counter
    print(count) #printing the unique item counter
    
except:
    print('Unable to open file.', file_name) #if unable to open file 
    exit()
