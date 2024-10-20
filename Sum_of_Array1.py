#normal method
'''
def Sum_Array(arr):
    count=0
    for i in arr:
        count=count+i
    return count


arr=[1,2,3]
n=len(arr)
a=Sum_Array(arr)
print(a)
'''

#using sum()

# arr=[1,2,3]
# print(sum(arr))


#Using the reduce method. Array.reduce() 
#uses of lambda func

# from functools import reduce
# def Sum_Array(arr):
#     sum=reduce(lambda a,b:a+b,arr)
#     return sum

# arr=[1,2,3]
# a=Sum_Array(arr)
# print(a)


#Using enumerate function 
# list1 = [1,2,3];s=0
# for i,a in enumerate(list1): 
#     s+=a 
# print(s)


#Using Divide and conquer

def func(arr,low,high):
    if low==high:
        return arr[low]
    mid=(high+low)//2
    
    left_sum=func(arr, low, mid)
    right_sum=func(arr,mid+1,high)
    return left_sum+right_sum

arr=[1,2,3,10]
r=func(arr,0,len(arr)-1)
print(r)

#Using counter method





from collections import Counter
 
arr = [12, 3, 4, 15]
c = Counter(arr)
sum = 0
 
for key, value in c.items():
    sum += key * value
 
print("Sum of the array is", sum)