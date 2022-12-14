# P6: Slicing & Dicing files
# Problem Statement: Write a program to prompt for a file name, and then read through the file and look for lines of the form: X-DSPAM-Confidence: 0.8475
# @author: Atishay Jain
# Date: 17th October 2022

#importing os module which helps in creating and removing a directory (folder), fetching its contents, changing and identifying the current directory, etc.
import os

#defining a function for slicing and dicing the file and its content.
def slicing_dicing():
    try:
        fname = input("Enter the file name:")
        f = open(fname, "r")
        file_content = f.readlines()

        file_length = os.path.getsize(f)

        if file_length == 0:
            print("File is empty") #user has entered an empty file with no characters.
        else:
            #initializing variables for count and spamconfidence
            count = 0
            spamConfidence = 0
            for line in file_content: #reading line by line in file_content
                if line.startswith('X-DSPAM-Confidence:'):
                    count = count + 1
                    x=line.find(".")
                    num= float(line[x:])
                    spamConfidence = spamConfidence + num
                else:
                    continue
            AvgSC = (spamConfidence / count)    
            AvgSC = round(AvgSC, 4)
            print(f'The average Spam Confidence is: {AvgSC}')
    except:
        print ("Error! The file might be missing.")

if __name__ == "__main__":
    slicing_dicing() #calling the function from the main function.


