
#mainclass
class Character(object):
    def __init__(self, name):
        self.health=100
        self.name = name
    def printName(self):
        print (self.name)



#subclasses
class NPC(Character):
    def __init__(self,name,npc):
        super(NPC,self).__init__(name)
        self.enemy = Enemy(npc)
        self.ally = Ally(npc)

class Enemy:
    def __init__(self,name):
        self.name=Enemy
        self.attackDamage=5
    def printDamage(self):
        print(self.attackDamage)
        
class Ally:
    def __init__(self,name):
        self.name=Ally

class PC(Character):
    def __init__(self,name,characterName):
        super(PC,self).__init__(name)
        self.archer = Archer(characterName)
        self.butcher = Butcher(characterName)
        self.greenlantern = GreenLantern(characterName)

class Archer:
    def __init__(self,characterName):
        self.name=characterName

class Butcher:
    def __init__(self,characterName):
        self.name=characterName

class GreenLantern:
    def __init__(self,characterName):
        self.name=characterName



#Lager variabler med navn for hver subclass
butch = PC("Butcher","BUTCHERRRR")
green= PC("Green Lantern","GrønnMann")
arc = PC("Archer","Buemann")


slem = NPC("Enemy","NPC")
dmg = Enemy("")
snill = NPC("Ally", "NPC")


#outputter navn for hver subclass
slem.printName()
dmg.printDamage()
snill.printName()
print(dmg.attackDamage)

arc.printName()
butch.printName()
green.printName()


# For å sjekke hvor mange subclasser en mainclass har
print(Character.__subclasses__())


'''

Lets learn python Eksempel!

class Blacksmith(Character):
    def __init__(self, name, forgeName):
        super(Blacksmith, self).__init__(name)
        self.forge=Forge(forgeName)

class Forge:
    def __init__(self,forgeName):
        self.name=forgeName


bs = Blacksmith("Bob","Rock\'s Forge")
bs.printName()
print(bs.forge.name)
print(bs.health)
'''
