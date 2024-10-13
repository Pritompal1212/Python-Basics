#Given a number x, determine whether the given number is 
#Armstrong number or not. A positive integer of n digits is 
#called an Armstrong number of order n (order is number of digits) if.

'''
num=int(input("enter num: "))
old=num
ans=0
while(num>0):
    lastdigit=num%10
    num=num//10
    cube=lastdigit**3
    ans=ans+cube

if (ans==old):
    print(ans)
else :
   print("Error")
'''


#using func
'''
def power(x, y):
     
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
         
    return x * power(x, y // 2) * power(x, y // 2)
 
# Function to calculate order of the number
def order(x):
 
    # Variable to store of the number
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10
         
    return n
 
# Function to check whether the given 
# number is Armstrong number or not
def isArmstrong(x):
     
    n = order(x)
    temp = x
    sum1 = 0
     
    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp // 10
 
    # If condition satisfies
    return (sum1 == x)
 
# Driver code
x = 153
print(isArmstrong(x))
 
x = 1253
print(isArmstrong(x))
'''


#using return value
'''

def is_armstrog(number):
    return    sum(int(digit)**len(str(number)) for digit in str(number)) ==number

num=156
if is_armstrog(num):
    print(f"true")
else:
    print(f"false")
'''
   
   
   
#using string manipulation
'''
This approach involves converting the input number into a string and iterating through
each digit in the string. For each digit, we raise it to the power of the number of digits
in the input number, and sum up the results. If the final sum equals the input number,
it is an Armstrong number.
'''

def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit)**n
    if sum == num:
        return True
    else:
        return False
num=153
print(is_armstrong(num))

