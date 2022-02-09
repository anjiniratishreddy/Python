######## arithimatic operators ###########
#addition
print(10 + 5)

# subtraction

#multiplication
print(10 * 5)

#division /

# modulus %

# exponential **

## floor division // - returns a round off or whole number
print(3 // 2) # returns 1 (instead of 1.5)

########### assignement operator ##############
#    =
#    +=
#    -=
#    *=
#    /=
#    %=
#    //=
#    **=


############# comparision operators ###############

#  ==
#  !=
#  >
#  <
#  >=
#  <=


########### logical operators #################

# and, or, not - to combine comparisin relationship




########### identity operators ###########
# is, is not
# these are used to compare objects. 
# whether they are same objects with same memory location
x = 'Ratish'
y = 'Ratish'
z = 'Ratish P'
print(x is y) # returns True - strange: python might just not create a duplicate string in memory and just assigns a different variable for the same memory
print(x is z) # false
print(x is not z) # true


########## membership operators ###############

# used to test the membership of a sequence is present in object such as string, list, tuples and dictionaries


########### Bitwise operators ##########

print(bin(0x38))

## &, |, ^ xor, ~ not, << left shift, >> right shift