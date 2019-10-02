#eksempel 1
def outside():
    x = 5
    def printHam():
        print (x)
    return printHam

MyFunc= outside()
MyFunc()

# eksempel 2
def addOne(myFunc):
    def addOneInside():
        return myFunc() + 1
    return addOneInside



def oldFunc():
    return 3

#her kan man også override en annen funksjon ved å fylle inn navnet på den som en ny type.
#Altså, 
# oldFunc = addOne(oldFunc)
# print(oldFunc())
#Dette vil da overskrive oldFunc ved å legge til +1 fra addOne funksjonen. så output blir 4
newFunc= addOne(oldFunc)
print (oldFunc(),newFunc())

def printHam():
    y = "ham"
    def ham(*args,**kwargs):
        print(*args,**kwargs)
    return ham

x=printHam()
x()

