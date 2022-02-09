########## while 

i=9
while i >=0:
    print(i)
    i -= 1
    if i > 4:
        continue
    else:
        break



########## for

fruit = ["banana","apple",'kiwi','pear']

for item in fruit:
    if item != 'kiwi':
        print(item)
        continue ## stops current iteration
    else:
        break # terminates the loop

