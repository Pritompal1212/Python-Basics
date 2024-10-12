#A = P(1 + R/100) t 

'''
def com_in(P,R,t):
    A = P*((1 + R/100)**t)
    CI=A-P
    print(CI)
    
com_in(10000,10.25,5)
'''

#take input from user

p=int(input("enter p: "))
r=float(input("enter r: "))
t=int(input("enter t: "))

def com_in(p,r,t):
    a=p*((1+r/100)**t)
    ci=a-p
    print(ci)
com_in(p,r,t)


#using for loop
'''
def com_in(p,r,t):
    a=p
    for i in range(t):
        a=a*(1+r/100)
    ci=a-p
    print(ci)
com_in(1200,5.4,2)
'''