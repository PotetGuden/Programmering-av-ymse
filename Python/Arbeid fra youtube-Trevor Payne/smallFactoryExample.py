BaseClass = type("BaseClass",(object,),{})      #Bare en annen metode for å lage classes

@classmethod
def Check1(self,myStr):
    return myStr == "ham"

@classmethod
def Check2(self,myStr):
    return myStr == "Sandwich"



C1 = type("C1",(BaseClass,),{"x":1,"Check" : Check1})
C2 = type("C2",(BaseClass,),{"x":30, "Check" : Check2 })

def MyFactory(myStr,myBool):
    for cls in BaseClass.__subclasses__():
        if cls.Check(myStr):
            return cls()
    return C1() if myBool else C2()    

m =MyFactory("Ham", True)
v =MyFactory("Sandwich", False)

''' 
def MyFactory(myBool):                          # Lager en funksjon med Boolean(true/false)
     return C1() if myBool else C2()             #obv.. "if true"
m= MyFactory(True)
v= MyFactory(False)
'''

print(m.x,v.x)
print(m,v)