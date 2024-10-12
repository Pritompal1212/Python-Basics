
#1
'''
num1=5
num2=3
sum=num1+num2
print("add both then",sum)
'''

'''
a1=5
b1=6.6
pum=float(a1)+float(b1)
print(pum)
'''

'''
#using function
def add_two(a2,b2):
    sum=a2+b2
    return sum
result=add_two(20,50)
print("------------------------------------",result)
'''

'''
#using .add()
a3=100
b3=100

import operator
pum=addition1.add(a3,b3)
print(pum)
'''

'''
# using .add() in set 
add2no={1,2,3,4}
add2no.add(50)
print(add2no)
#we cannot add multiple value in one "additon_2No.add(50,60,90)" operator
add2no.add(60)
print(add2no)
'''

'''
#using lambda function 
addtwo=lambda x,y:x+y
nm1=30
nm2=50
rslt=addtwo(nm1,nm2)
print("final addition",rslt)
'''

#using class in python
class Calculator:
    def add(self, num1, num2):
        return num1 + num2

# Example usage:
calc = Calculator()
result = calc.add(10, 20)
print(result)