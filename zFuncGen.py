import numpy as np
import random

class ZFuncGen:
    """ Represents the function to generate the 3D 
    """
    def __init__(self, deg:int):
        # configure the function here
        self.deg = deg
        self.trig = [bool(random.randint(0,1) == 1) for i in range(deg)] # type of trig function (sin or cos)
        self.a = [7*(random.random()+1) for i in range(deg)]
        self.b = [(random.random()+1) for i in range(deg)]
        self.c = [7*(random.random()+1) for i in range(deg)]
        self.d = [7*(random.random()+1) for i in range(deg)]
        # a*cos(b*(t+c))+d OR a*sin(b*(t+c))+d

    def getWithRange(self, zline):
        newZLine = self.a[0]*np.sin(self.b[0]*(zline+self.c[0]))+self.d[0]
        for i in range(1,self.deg):
            if self.trig[i]: # sin vs cos
                newZLine += self.a[i]*np.sin(self.b[i]*(zline+self.c[i]))+self.d[i]
            else:
                newZLine += self.a[i]*np.cos(self.b[i]*(zline+self.c[i]))+self.d[i]
        return newZLine