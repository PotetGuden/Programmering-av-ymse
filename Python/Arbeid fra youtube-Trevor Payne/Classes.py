import OverridingExample as O


class Overriding(Baseclass):
    def __init__(self):
        super(Overriding, self).__init__()
        self.x=17


i=Overriding()
print(i.x)

from inspect import getsource
getsource(i)
print(getsource(i))