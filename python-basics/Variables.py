#variables are case sensitive in python

import string


Age = 24
age = 25
AGE = 26

#all these are different

name = 'Ratish'

print(type(age))
#variable can change its type after creating it
age = 'Twenty Five'
print('type after changing '+str(type(age)))
print(type(name))

a,b,c = "apple","ball","cat" #indivisual assignment at the same time
x = y = z = "Fruit" #one value to multiple variable