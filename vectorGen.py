import numpy as np
import math
import time
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import random
from zFuncGen import *

class CONST:
    POLY_DEG_2_2D       = 0
    POLY_DEG_3_2D       = 1
    SINSQR_PLUS_COS     = 2

class RAND:
    SCALE_FACTOR = 5

class VectorFunc:
    """ Represents a randomized 2D function given starting point, direction, type of function, and domain """

    def __init__(self, curveType:int, point:tuple, dir:tuple, domain:list, ts:tuple):
        """Creates Vector Generator

        Args:
            curveType (int): type of curve (use constants)
            point (tuple): start point
            dir (tuple): start direction
            domain (np list): points to feed functions
            ts (tuple): start and end ts

        Returns:
            xline: np list, function
            yline: np list, function
            endpoint: tuple, endpoint 
            enddir: tuple, endpoint direction
        """
        self.x, self.y = point # start point
        self.xp, self.yp = dir # start direction
        self.ti, self.tf = ts # start and end t
        self.domain = domain
        self.curveType = curveType
    
    def gen(self):
        match self.curveType:
            case CONST.POLY_DEG_2_2D: 
                return self.polyDeg_2_2D()
            case CONST.POLY_DEG_3_2D:
                return self.polyDeg_3_2D()
            case CONST.SINSQR_PLUS_COS:
                return self.sinSqrPlusCos()

    def polyDeg_2_2D(self):
        """In the form:

        r(t) = <at+b, ct^2+d>

        Returns:
            np list: xline, yline, endpoint, enddir
        """
        t,x,xp,y,yp = self.ti,self.x,self.xp,self.y,self.yp
        
        a = xp
        if t != 0: c = yp/(2*t)
        else: # t is zero, you can do whatever you want
            c = random.randint(-RAND.SCALE_FACTOR,RAND.SCALE_FACTOR) 
        b = x-a*t
        d = y-c*pow(t,2)

        xline = a * self.domain + b
        yline = c * np.power(self.domain, 2) + d

        endpoint = (a*self.tf+b, c*pow(self.tf, 2)+d)
        enddir = (a,2*c*self.tf)
        #print(xline,yline,endpoint,enddir)
        return xline, yline, endpoint, enddir


    def polyDeg_3_2D(self):
        """In the form:

        r(t) = <at+b, ct^3+d>

        Returns:
            np list: xline, yline, endpoint, enddir
        """
        t,x,xp,y,yp = self.ti,self.x,self.xp,self.y,self.yp
        
        a = xp
        if t != 0: c = yp/(3*pow(t,2))
        else: # t is zero, you can do whatever you want
            c = random.randint(-RAND.SCALE_FACTOR,RAND.SCALE_FACTOR)
        b = x-a*t
        d = y-c*pow(t,3)

        xline = a * self.domain + b
        yline = c * np.power(self.domain, 3) + d

        endpoint = (a*self.tf+b, c*pow(self.tf, 3)+d)
        enddir = (a,3*c*pow(self.tf, 2))
        return xline, yline, endpoint, enddir

    def sinSqrPlusCos(self):
        """In the form:

        r(t) = <at + b, c*sin^2(t) + d*cos(t)>

        Returns:
            np list: xline, yline, endpoint, enddir
        """
        t,x,xp,y,yp = self.ti,self.x,self.xp,self.y,self.yp
        
        # redo this
        a = xp
        b = x-xp*t
        try:
            if t == 0:
                return self.polyDeg_3_2D()
            else:
                d = (4*y-np.tan(t))/(np.tan(t)*np.sin(t) + 4*np.cos(t))
                c = (yp + d*np.sin(t))/(np.sin(2*t)) 
        except: 
            # if it doesn't work, just use another one
            return self.polyDeg_3_2D()

        xline = a * self.domain + b
        yline = c * np.power(np.sin(self.domain), 2) + d * np.cos(self.domain) # we know this is still wrong

        endpoint = (a * self.tf + b, c * np.power(np.sin(self.tf), 2) + d * np.cos(self.tf))
        enddir = (a,c*np.sin(self.tf*t)-d*np.sin(self.tf))
        return xline, yline, endpoint, enddir

class GenCircuit:

    def __init__(self, numPieces:int, deg:int):

        fig = plt.figure()
        ax = plt.axes(projection='3d')

        self.zFunc = ZFuncGen(deg)

        colors = ['gray','orange','blue','red','yellow','purple','green'] # need to randomize colors differently
        endpoint = (0,0)
        enddir = (1,0)

        for i in range(numPieces):
            zline = np.linspace(5*i, 5*(i+1), 1000)
            curve = VectorFunc(self.randVectorFunc(), endpoint, enddir, zline, (5*i,5*(i+1)))
            xline, yline, endpoint, enddir = curve.gen()
            ax.plot3D(xline, yline, self.zFunc.getWithRange(zline), colors[i%7])
        
        plt.show()

    def randVectorFunc(self):
        r = random.random()
        if (r < 0.7):
            return CONST.SINSQR_PLUS_COS
        else:
            return CONST.POLY_DEG_2_2D if bool(random.randint(0,1)) else CONST.POLY_DEG_2_2D