def myFun():
    print('Function basic')

myFun()

def myFun(fname):
    print('first name is '+fname)

myFun('ratish')

def myFun(fname='rakesh', sname='p'):
    print('first name is ' + fname + '. last name is '+sname)

myFun('ratish','p')

myFun(sname='p',fname='ratish')

myFun()


#arbitaty arguments
def yourFunc(*args):
    print(args)

yourFunc('1','2',3) ##prints a tuple


#arbitary key word arguments
def theirFunc(**args):
    print(args)

theirFunc(fname='ratish',sname='p',age='25') #prints a dictionary


def mul(a,b):
    return a * b

print(mul(2,3))


#type safety
def div(divident: int, divisor: int) -> str:
    return str(divident/divisor)


print(div(8,2))