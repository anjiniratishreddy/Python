#it is collection which is ordered and unchangeable


myTuple = ('apple','orange','banana')
myTuple[1] = 'grape' # returns an error

myTuple2 = ('Hello') # this is of type string not tuple
myTuple3 = ('Hello',) # this is a tuple

#  Update Tuple
# tuples by default are immutable
# So you convert the tuple to list and perform modificaions and convert it back to tuple

temp = list(myTuple) #tuple is converted to list
myTuple = tuple(temp) # list is converted to tuple

##### unpack a tuple

(green, red, yellow) = myTuple # individual assignment
(green, *restOfThem) = myTuple # green will get apple, rest all will be assigned to restOfThem



### loop through a tuple

for i in myTuple:
    print(i)

for i in range(0, len(myTuple)):
    print(i)

###### jon tuples

otherTuple = (1,2,3)
newTuple = myTuple + otherTuple
print(newTuple)


newTuple2 = newTuple * 2 # tuple will be repeated
