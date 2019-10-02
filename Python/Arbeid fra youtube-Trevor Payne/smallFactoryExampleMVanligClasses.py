class BaseClass(object):
    pass

@classmethod
def Check1(self,myStr):
    return myStr == "Ham"

@classmethod
def Check2 (self,myStr):
    return myStr == "sandwich"


class C1(BaseClass):
    x=1
    Check= Check1
class C2(BaseClass):
    x=30
    Check= Check2


def MyFactory(myStr,myBool):                          # Lager en funksjon med Boolean(true/false)
     for cls in BaseClass.__subclasses__():           # for hver "subclass" i BaseClass
         if cls.Check(myStr):                         
             return cls()
     return C1() if myBool else C2()           #obv.. "if true"
m= MyFactory("Ham",True)
v= MyFactory("sandwich",False)

print(m.x,v.x)