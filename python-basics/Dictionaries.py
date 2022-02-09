myDic = {
    "id":1,
    "name":"Ratish"
}


print(myDic)
print(myDic["name"])
print(myDic.keys())
print(myDic.values())
print(myDic.items()) # returns key value pairs as list of arrays


myDic["name"] = "Anjini" # it updates the value
myDic.update({"name":"Ratish"})
print(myDic)


#add a new key value pair
myDic["salary"] = 1000
myDic.update({"salary":1000})

#remove an item
myDic.pop('salary')
myDic.popitem() #removes the item in order
myDic.clear()

#delete
del myDic["salary"]
del myDic


########## iterate a dictionary

for x in myDic:
    print(x)#gives only keys

for x in myDic:
    print(myDic[x]) #gives values

for x in myDic.values():
    print(x)

for x in myDic.items():
    print(x) # results one by one key value per iteration

for x,y in myDic.items():
    print(x,y)



################ copy dictionary

newDic = {myDic}


############## nested dictionary

nestDic = {
    "emp1":{
        "name":"ratish",
        "age":25
    },
    "emp2":{
        "name":"anjini",
        "age":25
    }
}

