'''
def max_num(a,b):
    if a>=b:
        return a
    else:
        return b
rslt=max_num(-1,-4)
print(rslt)
'''

'''
#using max func
rslt=max(90,99)
print(rslt)
'''

#using tarnary syntax
# <true_value> if <condition> else <false_value>

y=90
x=88
'''rslt="max" if x>y else "min"
print(rslt)'''
print(x if x >= y else y)


#using lambda func
#syntax = lambda arguments: expression
'''
max_value=lambda x,y: x if x>=y else y
x=20
y=90
rslt=max_value(x,y)
print(rslt)
'''


#using list
'''
a=4
b=6
z=[a if a>=b else b]
print(z)
'''


#using short() method
'''
a=15
b=70
z=[a,b]
z.sort()
print(z[-1])
'''
