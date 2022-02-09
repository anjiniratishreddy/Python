#Sets are used to store multiple items in a single variable
#set is unordered, unchangable, unindexable and do not allow duplicates

mySet = {'apple','banana','orange'}
# print(mySet[0]) --> cant do it
#cant have duplicates as well

for i in mySet:
    print(i)



print('apple' in mySet)

mySet.add('kiwi')

newSet = {1,2,3}

mySet.update(newSet)

#remove
mySet.remove('banana') # if banana is not found, then it'll throw error
mySet.discard('banana')# error will not be thrown if banana is not found

#clear
mySet.clear() 

#delete
del mySet


########## join
yourSet ={'a', 'b', 'c'}
theirSet = {'d','c','e'}
set1 = yourSet.union(newSet)


yourSet.intersection_update(theirSet) #takes only common items and updates in yourSet. doest return anything

set2 = yourSet.intersection(theirSet) # does the same but retuens a set


yourSet.symmetric_difference_update(theirSet) #non common items. doesnt return anything
set3 = yourSet.symmetric_difference_update(theirSet) #non common items. returns a set


