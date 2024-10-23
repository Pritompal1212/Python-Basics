#normal approch
'''
arr=[1,2,3,4,5,6,7,8]
st=0
en=len(arr)-1
while st<=en:
    temp=arr[st]
    arr[st]=arr[en]
    arr[en]=temp
    st+=1
    en-=1
st1=0
en1=len(arr)-2
while st1<=en1:
    temp = arr[st1]
    arr[st1] = arr[en1]
    arr[en1] = temp
    st1+=1
    en1-=1
for i in range(len(arr)):
    print(arr[i],end=" ")
'''

# function for normal approch
'''
def reverse_array(arr, start, end):
    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

arr = [1, 2, 3, 4, 5, 6, 7, 8]

reverse_array(arr, 0, len(arr)-1)

reverse_array(arr, 0, len(arr)-2)

for i in range(8):
    print(arr[i], end=" ")
'''


#using double shift 

# function to rotate array by d elements using temp array
def rotateArray(arr, n, d):
	temp = []
	i = 0
	while (i < d):
		temp.append(arr[i])
		i = i + 1
	i = 0
	while (d < n):
		arr[i] = arr[d]
		i = i + 1
		d = d + 1
	arr[:] = arr[: i] + temp
	return arr


# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))



print("  musst neeeed toooo waaatchhhh viiiiidddeeeooo ffffffooorrr tttttthhhhhhiiiiissssss ttttttooooooopppppppiiiiiiicccccccc ")