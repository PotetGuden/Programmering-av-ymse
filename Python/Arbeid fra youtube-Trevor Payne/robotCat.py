from random import randint
from time import clock


##========================================================
class State(object):
    pass

class Walk(State):
    def Execute(self):
        print("The cat in walking!")

class Sleep(State):
    def Execute(self):
        print("The cat is sleeping")

class Meow(State):
    def Execute(self):
        print("The cat is meowing..")

##========================================================
class Transition(object):
    def __init__(self,toState):
        self.toState = toState

    def Execute(self):
        print("Transitioning...")

##========================================================
class SimpleFSM(object):
    def __init__(self,char):
        self.char = char
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.trans = None
        # self.prevState = None

    def SetState(self, stateName):
        self.curState = self.states[stateName]

    def Transition (self,transName):
        self.trans = self.transitions[transName]

    def Execute(self):
        if(self.trans):
            self.trans.Execute()
            self.SetState(self.trans.toState)
            self.trans = None
        self.curState.Execute()
##========================================================

class Char(object):
    def __init__(self):
        self.FSM = SimpleFSM(self)
        self.Walk = True

##========================================================

if __name__ == "__main__":
    cat = Char()

    cat.FSM.states["Walk"] = Walk()
    cat.FSM.states["Sleep"] = Sleep()
    cat.FSM.states["Meow"] = Meow()
    cat.FSM.transitions["toWalk"] = Transition("Walk")
    cat.FSM.transitions["toSleep"] = Transition("Sleep")
    cat.FSM.transitions["toMeow"] = Transition("Meow")

    cat.FSM.SetState("Walk")

    for i in range(10):
        startTime = clock()
        timeInterval = .5
        randomInteger = randint (1,3)
        
        while (startTime + timeInterval > clock()):
            pass
        if (randint(0,2)):
            cat.FSM.Transition("toSleep") 
            cat.Meow = False
            cat.Walk = False
        elif (randint(3,4)):
            cat.FSM.Transition("toMeow")
            cat.Sleep = False
            cat.Walk = False
        else:
            #Mangler å få til toWalk og toMeow
            cat.FSM.Transition("toWalk")
            cat.Walk = True
        cat.FSM.Execute()