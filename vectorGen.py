import numpy as np
import math
import time
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import random
from zFuncGen import *

class CONST:
    POLY_DEG_1_2D = 1
    POLY_DEG_2_2D = 2
    POLY_DEG_3_2D = 3
    POLY_DEG_4_2D = 4
    POLY_DEG_5_2D = 5

class RAND:
    SCALE_FACTOR = 5

class VectorFunc:
    """ Represents a randomized 2D function given starting point, direction, type of function, and domain """

    def __init__(self, curveType:int, point:tuple, dir:tuple, domain:list, ts:tuple):
        """_summary_

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
            case CONST.POLY_DEG_1_2D:
                return 0 #self.polyDeg_1_2D()
            case CONST.POLY_DEG_2_2D: 
                return self.polyDeg_2_2D()
            case CONST.POLY_DEG_3_2D:
                return self.polyDeg_3_2D()
            case CONST.POLY_DEG_4_2D:
                return 0 #self.polyDeg_4_2D()

    def polyDeg_2_2D(self):
        """In the form:

        r(t) = <at+b, ct^2+d>

        Returns:
            np list: xline, yline
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
            np list: xline, yline
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
        return CONST.POLY_DEG_2_2D if bool(random.randint(0,1)) else CONST.POLY_DEG_3_2D