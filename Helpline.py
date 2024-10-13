#gitub
# git init
# git add .
# git commit -m"message"
# git status

#link to practice
#   https://www.geeksforgeeks.org/python-programming-examples/ 

'''For Function'''
#def <func_Name>(parameter):


#1 for i in range()
#2 for i in nums


'''Tarnary operator '''
# <true_value> if <condition> else <false_value>


#using lambda func
#syntax = lambda arguments: expression 


'''Factorial Function in Maths
In Python, math module contains a number of 
mathematical operations,which can be performed
with ease using the module. *math.factorial()* function
returns the factorial of desired number.'''
#import math 
#math.factorial()


#using numpy.prod()
'''This Python code calculates the factorial of n using NumPy.
It creates a list of numbers from 1 to n, computes their product
with numpy.prod(), and prints the result.'''


num=153
origin = num
ans = 0
while(num>0):
    lastdigit = num %10
    num = num//10
    cub = lastdigit**3
    ans = ans + cub

if(ans == origin):
    print("yes")

else:
    print("no")
