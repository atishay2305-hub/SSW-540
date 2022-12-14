"""
P2 Assignment: Convert numeric scores to grades
Author: Atishay Jain
M.S. in Software Engineering
"""
"""
Problem Statement:Write a script that asks the user for a quiz score and converts that numeric score to a letter grade.
"""
try:
    quiz_score = float(input('enter the quiz score ')) #taking user input for quiz score 
#giving the range for quiz scores : 0 to 100
    if quiz_score >= 92 and quiz_score <=100: #when marks are in range(92,100)
        print("A")
    elif quiz_score > 89 and quiz_score <= 92: #when marks are in range(90,92)
        print("A-")
    elif quiz_score >= 87 and quiz_score <= 89: #when marks are in range(87-89)
        print("B+")
    elif quiz_score >= 83 and quiz_score <= 86: #when marks are in range(83-86)
        print("B")
    elif quiz_score >= 80 and quiz_score <= 82: #when marks are in range(80-82)
        print("B-")
    elif quiz_score >= 70 and quiz_score <=79: #when marks are in range(70-79)
        print("C")
    elif quiz_score > 0 and quiz_score < 70: #when marks are under 70 but above 0.
        print("F")
    elif quiz_score > 100: #range for marks is only from 0 to 100 inclusive.
        print("This value is not legally valid.") #invalid entry as legally one can have marks in range of 0 to 100 only.
except:
    print("Invalid Input") #any other value apart from the above given range will be counted as Invalid Input.


