import numpy as np
import math
import time
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import random

class CONST:
    POLY_DEG_1_2D = 1
    POLY_DEG_2_2D = 2
    POLY_DEG_3_2D = 3
    POLY_DEG_4_2D = 4
    POLY_DEG_5_2D = 5

class RAND:
    SCALE_FACTOR = 5

def test3D():
    """
    Tests a 3D plot
    """
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax = plt.axes(projection='3d')

    # Data for a three-dimensional line
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')
    plt.show()

    print("finished")

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
    
    def Gen(self):
        match self.curveType:
            case CONST.POLY_DEG_1_2D:
                return 0 #self.PolyDeg_1_2D()
            case CONST.POLY_DEG_2_2D: 
                return self.PolyDeg_2_2D()
            case CONST.POLY_DEG_3_2D:
                return self.PolyDeg_3_2D()
            case CONST.POLY_DEG_4_2D:
                return 0 #self.PolyDeg_4_2D()

    def PolyDeg_2_2D(self):
        """In the form:

        r(t) = <at+b, ct^2+d>

        Returns:
            np list: xline, yline
        """
        t,x,xp,y,yp = self.ti,self.x,self.xp,self.y,self.yp
        
        a = xp
        if t != 0: c = yp/(2*t)
        else: # t is zero, you can do whatever you want
            c = 1 # try 1 for now # random.randint(-RAND.SCALE_FACTOR,RAND.SCALE_FACTOR) 
        b = x-a*t
        d = y-c*pow(t,2)

        xline = a * self.domain + b
        yline = c * np.power(self.domain, 2) + d

        endpoint = (a*self.tf+b, c*pow(self.tf, 2)+d)
        enddir = (a,2*c*self.tf)
        print(xline,yline,endpoint,enddir)
        return xline, yline, endpoint, enddir


    def PolyDeg_3_2D(self):
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


class ZFuncGen:
    """ Represents the function to generate the 3D 
    """
    def __init__(self):
        print("Blah")

def firstTest():
    """
    From a parabola to a cubic polynomial
    """
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax = plt.axes(projection='3d')

    zline = np.linspace(0, 5, 1000)
    # try from a 2d parabola to a 3d
    curve = VectorFunc(CONST.POLY_DEG_2_2D, (0,0), (1,0), zline, (0,5))
    xline, yline, endpoint, enddir = curve.Gen()
    ax.plot3D(xline, yline, 1, 'orange')
    
    zline = np.linspace(5, 10, 1000)
    curve = VectorFunc(CONST.POLY_DEG_3_2D, endpoint, enddir, zline, (5,10))
    xline, yline, endpoint, enddir = curve.Gen()
    ax.plot3D(xline, yline, 1, 'gray')
    plt.show()

class GenFullList:
    def __init__(self, type:int, point:list=(0,0)):
        '''Assumed to start at (0,0)'''
    
    def Poly2D(self):
        return 0, 0 # return xLine, yLine

def main():
    #test3D() # testing 3D matplotlib 
    firstTest() # first junction made!

main()
