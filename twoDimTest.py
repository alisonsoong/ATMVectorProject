import numpy as np
import math
import time
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class CONST:
    POLY_DEG_2_2D = 1

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

    def __init__(self, type:int, point:list, dir:list, domain:list):
        match type:
            case CONST.POLY_DEG_2_2D: 
                return self.Poly2D()
    
    def Poly2D(self):
        return 0, 0 # return xLine, yLine

class ZFuncGen:
    """ Represents the function to generate the 3D 
    """
    def __init__(self):
        print("Blah")


class GenFullList:
    def __init__(self, type:int, point:list=(0,0)):
        '''Assumed to start at (0,0)'''
    
    def Poly2D(self):
        return 0, 0 # return xLine, yLine

def main():
    test3D() # testing 3D

main()
