#using for
#syntax = for variable in iterable:
'''
x=5

n=1
for i in range(n,x+1):
    n*=i
    
print(n)
'''

'''
#using recursive
def fact(n):
    if n==0 or n==1:
       return 1
    fact(n-1)
    return  n*fact(n-1)
#shortcut= return 1 if (n==1 or n==0) else n * factorial(n - 1) 
rslt=fact(3)
print(rslt)
'''


#using tarnery operator
# <true_value> if <condition> else <false_value>
'''
def fac(n):
    return 1 if n==1 or n==0 else n*fac(n-1)
r=fac(5)
print(r)
'''

#using math.factorial
'''Factorial Function in Maths
In Python, math module contains a number of 
mathematical operations,which can be performed
with ease using the module. *math.factorial()* function
returns the factorial of desired number.'''
'''
import math
def fac(n):
    return math.factorial(n)
r=fac(5)
print(r)
'''

#using numpy.prod()
'''This Python code calculates the factorial of n using NumPy.
It creates a list of numbers from 1 to n, computes their product
with numpy.prod(), and prints the result.'''

# import numpy
# x=5
# x=numpy.prod([i for i in range(1,n+1)])
# print(x) 
#pblm not run 


#Prime factorization to find factorial - taff for biggners
# Function to find prime factors of a number
def primeFactors(n):
    factors = {}
    i = 2
    while i*i <= n:
        while n % i == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
            n //= i
        i += 1
    if n > 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1
    return factors

# Function to find factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n+1):
        factors = primeFactors(i)
        for p in factors:
            result *= p ** factors[p]
    return result

# Driver Code
num = 5
print("Factorial of", num, "is", factorial(num))