#P8
# Author: Atishay Jain
# Description:Python program that prompts the user for the name of a file with an arbitrary ASCII document, reads the file, and prints a summary of the words in the document.
# The summary should include:
# Total words
# Total distinct words
# The top 25 most frequent words and counts (You do NOT need to handle ties.  Just pick the top 25)
# Character frequency sorted from most frequent to least frequent characters

from msvcrt import kbhit
import os
from pathlib import Path
from platform import freedesktop_os_release
from string import punctuation
from operator import itemgetter
from collections import defaultdict

try:
    name = input("Enter the name of the file.")
    mypath = Path(name)
except:
    print("Please enter a valid name or the file could not be located.")

#function to have the total words, total characters
def Counter():
    try:
        file = print("Enter the file name")
        f = open(mypath)
        f.close()
    except:
        print("File not found")
    wordcount = 0 #number of words in the line initialized to 0
    line = []
    Freq = 0 #character frequency initialized to 0
    Worddict = defaultdict(int) #int because it will increase the count by 1 later when one word gets added
    Chardict = defaultdict(int) #default dictionaries to store characters from words

    with f as stream:
        file = list(stream)
    for i in range(len(file)):
        file[i] = file[i].lower() #converting all characters to lowercase of the words
        line = file[i].split() #splitting the words in order to count them
        punc = str.maketrans({key: None for key in punctuation})
        file[i] = file[i].translate(punc)
        for ch in file[i]:
            if ch in Chardict:
                Chardict[ch] = Chardict[ch] + 1
            else:
                Chardict[ch] = 1
        print(line)
        wordcount += len(line)
        for w in line:
            Worddict[w] += 1
        Words = len(Worddict)
        return Words  
    s = sorted(Worddict.items(), key=itemgetter(1), reverse = True)

    Freq = sorted(Chardict.items(), key = itemgetter(1), reverse=True)
    print("The total words are: " + str(wordcount))
    print("There are distinct and unique words: " + str(Worddict))
    print("The top 25 words are: " + s[:25])
    for y in range(len(Freq)):
        print(str(i+1), Freq[i])

if __name__ == "__main__":
    Counter() #calling the function


