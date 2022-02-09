x = "Ratish" # A string
y = 'Ratish' # A string

# Multiline string - use dog string
z = """
Python supports single line string
and multilined string as well
"""
################# A string is basically array of charachters - ther is no char data type in python

print(x[0]) # Returns R

############ Iterate a string

for c in x:
    print(c)

# Returns 
# R a t i s h - line by line

########### look in the string - 'in' oprator

print('ti' in x) # returns true
if "ti" in X:
    print('ti is present in x')

############### Concatination

x2 = 'P'
name = x + ' ' + x2 
print(name) # returns Ratish P

############### slicing a string - like substring in python its just '[]'

print(x[1:5]) # returns 'atis'
print(x[:5]) # returns 'Ratis'


############### formatting string ############

age = 25
salary = 1000
print(x+ ' ' + str(age))

# formatting using placeholder

print('My age is {} and my salary is {}'.format(age, salary)) # it is sequential - age will got to first placeholder and salary will go to 2nd
#returns My age is 25 and my salary is 1000

#but we can shuffle these
print('My age is {1} and my salary is {0}'.format(salary, age))
#indexing will help us to shuffle the order. need not always be squential


################### Escape charachters \ #########

print("My name is "Ratish"") # returns  error
print("My name is \"Ratish\"") # returns  My name is "Ratish"
print("My name is \\Ratish") # returns   My name is \Ratish
print("My name is \nRatish") # next line
#returns - My name is 
#Ratish
print("12345678\rRatish") #returns Ratish78 - carriage return
print("My name is \bRatish")# My name isRatish - backspace
#\t - tab
#\f - form feed
#\ooo - octal value
#\xhh - hex value


########## String Methods #############

caps = x.upper() ## returns RATISH - does not store the result in same variable
x.index('a') # returns an int with posotion of a 
x.replace('R','r') # ratish
b = "name,age,occuoation".split(',') # returns a list of 3 strings
 