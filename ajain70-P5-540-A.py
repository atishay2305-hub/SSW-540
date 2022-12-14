#P5: String manipulation
#Author: Atishay Jain
#Subject: Fundamentals of Software Engineering
#Date: 10/10/2022

# -------------------------------------------------------------------------------------------------------------------------------------------------------#

#here in the function "plural(s)", 's' is a variable that stores the String values
def plural(s): #defining a function that converts singular words into their plural words
    if s.endswith(('ay', 'iy' , 'oy' , 'uy' , 'ey')):
        return  s + 's'
    elif s.endswith(('by', 'cy', 'dy', 'fy', 'gy', 'hy', 'jy', 'ky', 'ly', 'my', 'ny', 'py', 'qy', 'ry', 'ty', 'vy', 'wy')):
        return s[:-1] + 'ies'
    elif s.endswith(('o', 'ch', 's' , 'sh' ,'x' ,'z')):
        return s + 'es' 
    else:
        return s + 's' #in any other case just append 's' in the end of the word
    
#taking a sample input list of elements to test the above function
List = ["monkey", "bush", "fox","donkey", "laptop", "fly", "atishay", "oho", "hach", ]

if __name__ == "__main__":
    for i in List: #iterating in all the elements present in the list 
        print(i, ':' , plural(i)) # printing the value of 'i'


