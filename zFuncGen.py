from re import I
import numpy as np
import random

class ZFuncGen:
    """ Generates z(t) to create the resulting 3D space curve
    """
    def __init__(self, deg:int, scale:tuple):
        '''
            creates the coefficients for a*cos(b*(t+c))+d OR a*sin(b*(t+c))+d
        '''
        # configure the function here
        self.deg = deg
        self.trig = [random.randint(0,1) for i in range(deg)] # type of trig function (sin or cos)
        self.a = [scale[0]*(random.random()+1) for i in range(deg)]
        self.b = [scale[1]*(random.random()+1) for i in range(deg)]
        self.c = [scale[2]*(random.random()+1) for i in range(deg)]
        self.d = [scale[3]*(random.random()+1) for i in range(deg)]

    def genZ(self, domain):
        # seed
        if self.trig[0]: zline = self.a[0]*np.sin(self.b[0]*(domain+self.c[0]))+self.d[0]
        else: zline = self.a[0]*np.cos(self.b[0]*(domain+self.c[0]))+self.d[0]

        for i in range(1,self.deg):
            if self.trig[i]: # sin vs cos
                zline += self.a[i]*np.sin(self.b[i]*(domain+self.c[i]))+self.d[i]
            else:
                zline += self.a[i]*np.cos(self.b[i]*(domain+self.c[i]))+self.d[i]
        return zline

    def genZP(self, domain):
        if self.trig[0]: zp = self.a[0]*self.b[0]*np.cos(self.b[0]*(domain+self.c[0]))
        else: zp = -self.a[0]*self.b[0]*np.sin(self.b[0]*(domain+self.c[0]))

        for i in range(1,self.deg):
            if self.trig[i]: # sin vs cos
                zp += self.a[i]*self.b[i]*np.cos(self.b[i]*(domain+self.c[i]))
            else:
                zp += -self.a[i]*self.b[i]*np.sin(self.b[i]*(domain+self.c[i]))
        
        return zp

    def genZPP(self, domain):
        if self.trig[0]: zpp = -self.a[0]*self.b[0]*self.b[0]*np.sin(self.b[0]*(domain+self.c[0]))
        else: zpp = -self.a[0]*self.b[0]*self.b[0]*np.cos(self.b[0]*(domain+self.c[0]))

        for i in range(1,self.deg):
            if self.trig[i]: # sin vs cos
                zpp += -self.a[i]*self.b[i]*self.b[i]*np.sin(self.b[i]*(domain+self.c[i]))
            else:
                zpp += -self.a[i]*self.b[i]*self.b[i]*np.cos(self.b[i]*(domain+self.c[i]))

        return zpp

    def genForCurvature(self, domain):
        return self.genZ(domain), self.genZP(domain), self.genZPP(domain)
