import time as t
from os import path

def createFile(dest):
    '''
    The script creates a text file the passed in location
    '''
    date = t.localtime(t.time())


    ## Filename = Month/day/year.txt
    name = "%d_%d_%d" %(date[1],date[2],(date[0]%100))
    
    
    if not (path.isfile(dest + name):
        f=open(dest + name, "w")
        f.write("jostein er kul\n"*30)
        f.close()

if __name__=='__main__':
    destination = "C:\\Users\\Joste\\OneDrive\\Desktop\\Lets learn Python\\"
    createFile(destination)
    input("DONE")

    
