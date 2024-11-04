# n=5

# for i in range(n):
#     print(" " * i, end="")
#     print("*" *(n-i))
    
    
#see an0ther way

n=5
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(n-i):
        print("*",end="")
    print()