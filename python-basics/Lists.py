myList = ['apple','banana','orange']
print(myList[1]) #banana
print(myList[-1])#orange
print(myList[0:2]) # returns a list apple, banana
print(myList[-3:-1])#apple banana

if "apple" in myList:
    print('apple is present in the list')
else:
    print('apple is not present')


# replace
myList[0:2] = ["grape","pine"]
print(myList)

#insert values in list
myList.insert(0,'apple')
print(myList)

#append one list with another list
otherList = ['kiwi','pear']
myList.extend(otherList)
print(myList)

#remove list item
myList.remove("pear")
## myList.remove(4) returns error - remove method needs literal value
myList.pop(3)
print(myList)

del myList[1]
print(myList)

myList.clear() ## clears all values
print(myList)



#### loop a list
myList2 = ['tomato','potato','beans']
for i in myList2:
    print(i)

for i in range(0,2):
    print(myList2[i])

#### sort
myList2.sort(reverse=True) #desc
myList.reverse() # simply reverses without any sorting

## copy
## we cant do list1 = list2 - both variables referes to same memory
myList = myList2.copy()
myList3 = list(myList2)


## join
myList4 = myList+myList2
myList4.extend(myList)

for x in myList:
    myList3.append(x)




