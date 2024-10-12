'''Simple interest formula is given by: Simple Interest = (P x T x R)/100
Where,P is the principal amount T is the time and R is the rate'''

#using func
'''
def simple_interest(p,t,r):    
    si = (p * t * r)/100
    print('The Simple Interest is', si)
    return si
simple_interest(8, 6, 8)
'''

#using input 

p=int(input("The principle is: ")) 
t=int(input("The time period is: ")) 
r=int(input("The rate of interest is: ")) 

si=(p*r*t)/100
print(si)


