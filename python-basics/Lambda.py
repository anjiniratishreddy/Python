lamFunc = lambda n,m : n*m

print(lamFunc(3,2))



# a function which returns a lambda 

def myFunc(n):
    return lambda x : x * n

double = myFunc(2) # lambda x: x *2
triple = myFunc(3) # lambda x: x *3