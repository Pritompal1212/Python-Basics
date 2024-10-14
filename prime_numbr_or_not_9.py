#trail division method
#need more study


'''
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):  
        #(n//2)+1 
        if n%i==0:
            return False
    return True
prime=is_prime(1)
print(prime)
'''

num = 11
# Negative numbers, 0 and 1 are not primes
if num > 1:
  
    # Iterate from 2 to n // 2
    for i in range(2, (num//2)+1):
      
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")