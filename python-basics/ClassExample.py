class Person:
    #properties
    firstName = ''
    lastName = ''
    gender = ''



    #methods
    ##self doesnt have to exactly 'self' it could be any name. first argument in every method in a class is a self-object of that class

    def __init__(self,fName, lName, gender) -> None: 
        self.firstName = fName
        self.lastName = lName
        self.gender = gender
        


    def PrintFullName(self):
        print(self.firstName+' '+self.lastName)
    



per1 = Person('ratish','p','male')
per2 = Person('rakesh','p','male')
print(per1.PrintFullName())
print(per2.PrintFullName())
    