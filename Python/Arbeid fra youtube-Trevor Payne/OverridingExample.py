from Classes import *

class BaseClass(object):
    def __init__(self):
        self.x= 5
    def printHam(self):
        print ("Hamasdsa")

class InClass(BaseClass):
    def test(self):
        print("LOL")
    def printHam(self):
        print("Ham2")




ham2= InClass()
ham2.printHam()
ham = BaseClass()
ham.printHam()






# For å sjekke hvor mange subclasser en mainclass har
print(BaseClass.__subclasses__())
