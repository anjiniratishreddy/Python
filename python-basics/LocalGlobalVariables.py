from pyrsistent import b


y = 'more than something' #global variable
z = 'global'
a = 'initial'
def oneFun():
    x = 'something' #local variable
    z  = 'local'
    global a
    a+' and appended' #now i can make changes to global variable
    #decleare a global variable in local mode
    global b
    #now b will be a global varable which is created from local mode
    print(x)
    print(y) #accessible here
    print(z) #local will be printed

oneFun()
# print(x) --> x is not accessable outside that function
print(z) #global will be printed