
# def fibbo(n):
#     t1 = 0  # First Fibonacci number
#     t2 = 1  # Second Fibonacci number
    
#     if n == 1:
#         return t1
#     elif n == 2:
#         return t2
    
#     for i in range(3,n+1):
#        nest =t1+t2
#        t1=t2
#        t2=nest
#        return t2
   
# r=fibbo(5)
# print(r)

def fibbo(n):
    t1 = 0  # First Fibonacci number
    t2 = 1  # Second Fibonacci number
    
    if n == 1:
        return t1
    elif n == 2:
        return t2
    
    for i in range(3, n + 1):  # Loop should go up to n (inclusive)
        next_num = t1 + t2  # Calculate the next Fibonacci number
        t1 = t2  # Shift t1 to t2
        t2 = next_num  # Shift t2 to next_num

    return t2  # Return the nth Fibonacci number

r = fibbo(5)
print(r)
