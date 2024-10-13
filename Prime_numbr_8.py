 #prime number print using loop and print range with given numbr

lower=1
upper=20
for i in range(lower,upper+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
     
            
'''
def prime(x,y):
    prime_list=[]
    for i in range(x,y):
        if i==0 or i==1 :
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j == 0:
                    break
            else:
                 prime_list.append(i)
    return prime_list
st=2
end=10
lst=prime(st,end)
if len(lst)==0:
    print("error guys")
else:
    print("success guys: ",lst)          
        

'''

# Function to check if a number is prime
'''
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
'''
