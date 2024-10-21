#using max func
'''
def func(arr,n):
    ans=max(arr)
    return ans

arr=[1,24,6,54,67,378]
n=len(arr)
r=func(arr,n)
print(r) 
'''

#using normally
'''
def fun1(arr,n):
    max=arr[0]
    for i in range(1,n):
        if arr[i]>max:
            max=arr[i]
    return max

arr=[1,7,6,77,741,86886,5777841,6545164987451]
n=len(arr)
r=fun1(arr,n)
print(r)
'''

#using sort
'''
def fun2(arr,n):
    arr.sort()
    return arr[n-1]

arr=[1,24,6,54,67,378]
n=len(arr)
r=fun2(arr,n)
print(r) 

'''

# using reduce()

'''
from functools import reduce
def largest(arr):
	ans = reduce(max, arr)
	return ans
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr)
print("Largest in given array ", Ans)
'''

# from functools import reduce

# def fun3(arr):
#     ans=reduce(max,arr)
#     return max
# arr=[1,24,6,54,67,378]
# n=len(arr)
# r=fun3(arr)
# print(r) 


#using operator
'''
# python program to find large number in the given array
import operator
# Initializing the list
arr = [2, 1, 7, 3, 0]
max=0

# printing the original list
print('The given array is:', arr)

#checking for large element
for i in arr:
if operator.gt(i,max):
	max=i

# printing the large number in the array
print('The biggest number in the given array is:', max)
'''


#using lambda
array = [10, 5, 20, 8, 15]

largest_element = max(array, key=lambda x: x)
print("Largest element in the array:", largest_element)
