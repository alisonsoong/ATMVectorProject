import numpy as np
import math
import time
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import matplotlib.colors as cls
import matplotlib as mpl
import mpl_toolkits.mplot3d as mpl3
import random
from zFuncGen import *

class CONST:
    POLY_DEG_2_2D       = 0
    POLY_DEG_3_2D       = 1
    SINSQR_PLUS_COS     = 2
    TREFOIL             = 3
    SIN_COS             = 4

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
    
    def gen(self, z, zp, zpp, curvatureDomain):
        self.z=z
        self.zp=zp
        self.zpp=zpp
        self.curvatureDomain = curvatureDomain
        match self.curveType:
            case CONST.POLY_DEG_2_2D: 
                return self.polyDeg_2_2D()
            case CONST.POLY_DEG_3_2D:
                return self.polyDeg_3_2D()
            case CONST.SINSQR_PLUS_COS:
                return self.sinSqrPlusCos()
            case CONST.TREFOIL:
                return self.trefoil()
            case CONST.SIN_COS:
                return self.sinCos()

    def polyDeg_2_2D(self):
        """In the form:

        r(t) = <at^2+b, ct^2+d>

        Returns:
            np list: xline, yline, endpoint, enddir
        """
        t,x,xp,y,yp = self.ti,self.x,self.xp,self.y,self.yp
        
        if t != 0: 
            a = xp/(2*t)
            c = yp/(2*t)
        else: # t is zero, you can do whatever you want
            a = random.randint(-RAND.SCALE_FACTOR,RAND.SCALE_FACTOR) 
            c = random.randint(-RAND.SCALE_FACTOR,RAND.SCALE_FACTOR) 
        b = x-a*pow(t,2)
        d = y-c*pow(t,2)

        xline = a * np.power(self.domain, 2) + b
        yline = c * np.power(self.domain, 2) + d

        endpoint = (a*pow(self.tf, 2)+b, c*pow(self.tf, 2)+d)
        enddir = (2*a*self.tf,2*c*self.tf)

        print("type of curve used: deg 2 poly curve. t val: ", t)
        print("calculated start point: ", (a*pow(t, 2)+b, c*pow(t, 2)+d))
        print("calculated start direction: ", (2*a*t,2*c*t))


        # calculate curvature
        z,zp,zpp=self.z,self.zp,self.zpp
        t = self.curvatureDomain
        xn = a*pow(t, 2)+b
        yn = c*pow(t, 2)+d
        csn = t/t

        return xline, yline, endpoint, enddir, xn, yn, csn


    def polyDeg_3_2D(self):
        """In the form:

        r(t) = <at^2+b, ct^3+d>

        Returns:
            np list: xline, yline, endpoint, enddir
        """
        t,x,xp,y,yp = self.ti,self.x,self.xp,self.y,self.yp
        
        if t != 0: 
            a = xp/(2*t)
            c = yp/(3*pow(t,2))
        else: # t is zero, you can do whatever you want
            a = random.randint(-RAND.SCALE_FACTOR,RAND.SCALE_FACTOR)
            c = random.randint(-RAND.SCALE_FACTOR,RAND.SCALE_FACTOR)
        b = x-a*pow(t,2)
        d = y-c*pow(t,3)

        xline = a * np.power(self.domain, 2) + b
        yline = c * np.power(self.domain, 3) + d

        endpoint = (a*pow(self.tf, 2)+b, c*pow(self.tf, 3)+d)
        enddir = (a*self.tf,3*c*pow(self.tf, 2))
        print("type of curve used: deg 3 poly curve. t val: ", t)
        print("calculated start point: ", (a*pow(t, 2)+b, c*pow(t, 3)+d))
        print("calculated start direction: ", (a*2*t,3*c*pow(t, 2)))

        # curvature
        z,zp,zpp=self.z,self.zp,self.zpp
        t = self.curvatureDomain
        xn = a*pow(t, 2)+b
        yn = c*pow(t, 3)+d
        csn = t/t

        return xline, yline, endpoint, enddir, xn, yn, csn

    def sinSqrPlusCos(self):
        """In the form:

        r(t) = <at + b, c*sin^2(t) + d*cos(t)>

        Returns:
            np list: xline, yline, endpoint, enddir
        """
        t,x,xp,y,yp = self.ti,self.x,self.xp,self.y,self.yp
        
        # redo this
        a = xp
        b = x-a*t
        try:
            if t==0:
                print("SWITCH")
                return self.polyDeg_3_2D()
            
            c = (yp + y*np.tan(t)) / (np.sin(2*t) + np.tan(t) * np.sin(t) *np.sin(t))
            d = (y-c*np.sin(t)*np.sin(t)) / (np.cos(t))

            if abs((c * np.power(np.sin(t), 2) + d * np.cos(t)) - y) > 1 or abs((c*np.sin(t*2)-d*np.sin(t)) - yp) > 1:
                d = (2*y-yp*np.tan(t))/(np.tan(t)*np.cos(t) + 2*np.cos(t))
                c = (yp + d*np.sin(t))/(2*np.sin(t)*np.cos(t)) 
            
            if abs((c * np.power(np.sin(t), 2) + d * np.cos(t)) - y) > 1 or abs((c*np.sin(t*2)-d*np.sin(t)) - yp) > 1:
                print("SWITCH")
                return self.polyDeg_3_2D()
        except: 
            # if it doesn't work, just use another one
            print("SWITCH")
            return self.polyDeg_3_2D()

        xline = a * self.domain + b
        yline = c * np.power(np.sin(self.domain), 2) + d * np.cos(self.domain) # now correct!

        endpoint = (a * self.tf + b, c * np.power(np.sin(self.tf), 2) + d * np.cos(self.tf))
        enddir = (a,c*np.sin(self.tf*2)-d*np.sin(self.tf))
        print("type of curve used: sin sq + sin curve. t val: ", t)
        #print(a,b,c,d)
        print("calculated start point: ", (a * t + b, c * np.power(np.sin(t), 2) + d * np.cos(t)))
        print("calculated start direction: ", (a,c*np.sin(t*2)-d*np.sin(t)))

        # curvature
        z,zp,zpp=self.z,self.zp,self.zpp
        t = self.curvatureDomain
        xn = a * t + b
        yn = c * np.power(np.sin(t), 2) + d * np.cos(t)
        csn = t/t

        return xline, yline, endpoint, enddir, xn, yn, csn
    
    def trefoil(self):
        """In the form:

        r(t) = <b+a*cos(1.5*t), d+c*cos(1.5*t)*sin(t)>

        Returns:
            np list: xline, yline, endpoint, enddir
        """
        t,x,xp,y,yp = self.ti,self.x,self.xp,self.y,self.yp
        
        # redo this
        try:
            a = xp/(-1.5*np.sin(1.5*t))
            b = x - a*np.cos(1.5*t)
            if t==0:
                print("SWITCH")
                return self.sinSqrPlusCos()
            c = yp/(-1.5*np.sin(1.5*t)*np.sin(t) + np.cos(1.5*t)*np.cos(t))
            d = y - c*np.cos(1.5*t)*np.sin(t)
        except: 
            # if it doesn't work, just use another one
            print("SWITCH")
            return self.sinSqrPlusCos()

        xline = b+a*np.cos(1.5*self.domain)
        yline = d+c*np.cos(1.5*self.domain)*np.sin(self.domain)

        endpoint = (b+a*np.cos(1.5*self.tf), d+c*np.cos(1.5*self.tf)*np.sin(self.tf))
        enddir = (-1.5*a*np.sin(1.5*self.tf), c*(-1.5*np.sin(1.5*self.tf)*np.sin(self.tf) + np.cos(1.5*self.tf)*np.cos(self.tf)))
        print("type of curve used: trefoil curve. t val: ", t)
        #print(a,b,c,d)
        print("calculated start point: ", (b+a*np.cos(1.5*t), d+c*np.cos(1.5*t)*np.sin(t)))
        print("calculated start direction: ", (-1.5*a*np.sin(1.5*t), c*(-1.5*np.sin(1.5*t)*np.sin(t) + np.cos(1.5*t)*np.cos(t))))

        # curvature
        z,zp,zpp=self.z,self.zp,self.zpp
        t = self.curvatureDomain
        xn = b+a*np.cos(1.5*t)
        yn = d+c*np.cos(1.5*t)*np.sin(t)
        csn = t/t

        return xline, yline, endpoint, enddir, xn, yn, csn
    
    def sinCos(self):
        """In the form:

        r(t) = <at+b, c*sint*cost+d>

        Returns:
            np list: xline, yline, endpoint, enddir
        """
        t,x,xp,y,yp = self.ti,self.x,self.xp,self.y,self.yp

        a = xp
        b = x-a*t
        try:
            if t==0:
                print("SWITCH")
                return self.polyDeg_2_2D()
            
            c = yp / (-np.sin(t)*np.sin(t) + np.cos(t)*np.cos(t))
            d = y - c*np.sin(t)*np.cos(t)

        except: 
            # if it doesn't work, just use another one
            print("SWITCH")
            return self.polyDeg_2_2D()

        xline = b+a*self.domain
        yline = c*np.sin(self.domain)*np.cos(self.domain) + d

        endpoint = (b+a*self.tf, c*np.sin(self.tf)*np.cos(self.tf) + d)
        enddir = (a, c*(-np.sin(self.tf)*np.sin(self.tf) + np.cos(self.tf)*np.cos(self.tf)))
        print("type of curve used: sincos curve. t val: ", t)
        #print(a,b,c,d)
        print("calculated start point: ", (b+a*t, c*np.sin(t)*np.cos(t) + d))
        print("calculated start direction: ", (a, c*(-np.sin(t)*np.sin(t) + np.cos(t)*np.cos(t))))

        # curvature
        z,zp,zpp=self.z,self.zp,self.zpp
        t = self.curvatureDomain
        xn = b+a*t
        yn = c*np.sin(t)*np.cos(t) + d
        xp = a*t/t
        xpp = 0*t/t
        yp = c*(np.cos(t)*np.cos(t) - np.sin(t)*np.sin(t))
        ypp = -2*c*np.sin(t)*np.cos(t) - 2*c*np.sin(t)*np.cos(t)

        csn = np.sqrt(np.power(np.multiply(yp, zpp) - np.multiply(ypp, zp),2) + np.power(np.multiply(xpp, zp) - np.multiply(xp, zpp),2) + np.power(np.multiply(xp, ypp) - np.multiply(xpp, yp),2)) / np.power(np.sqrt( np.power(xp,2) + np.power(yp,2) + np.power(zp,2) ),3)
        #csn = np.sqrt(pow((a*zpp*c*(-np.sin(t)*np.sin(t) + np.cos(t)*np.cos(t)) + 4*zp*c*np.cos(t)*np.sin(t)),2) + pow(-a*zpp,2) + pow(-4*a*c*np.cos(t)*np.sin(t), 2)) / (pow(np.sqrt(a*a+c*c*pow(-np.sin(t)*np.sin(t)+np.cos(t)*np.cos(t),2) + zp*zp),3))

        return xline, yline, endpoint, enddir, xn, yn, csn

class GenCircuit:

    def __init__(self, numPieces:int, deg:int):

        fig = plt.figure()
        ax = plt.axes(projection='3d')

        self.zFunc = ZFuncGen(deg,(random.randint(5,7),1,random.randint(5,7),random.randint(5,7)))

        colors = ['gray','orange','blue','red','purple','green']
        endpoint = (0,0)
        enddir = (5,1)
        type = -1

        x=np.array([0])
        y=np.array([0])
        z=np.array([0])
        cs=np.array([0])

        for i in range(numPieces):
            domain = np.linspace(5*i, 5*(i+1), 1000)
            
            print("cur color: ", colors[i%len(colors)])
            print("expected start point: ", endpoint)
            print("expected start direction: ", enddir)

            if i==0: type = CONST.SINSQR_PLUS_COS
            else: type = self.randVectorFunc(type)
            curve = VectorFunc(type, endpoint, enddir, domain, (5*i,5*(i+1)))

            zline = self.zFunc.genZ(domain)

            curvatureDomain = np.linspace(5*i, 5*(i+1), 40)
            zn, zp, zpp = self.zFunc.genForCurvature(curvatureDomain)

            xline, yline, endpoint, enddir, xn, yn, csn = curve.gen(zn, zp, zpp, curvatureDomain)
            x=np.concatenate((x,xn))
            y=np.concatenate((y,yn))
            z=np.concatenate((z,zn))
            cs=np.concatenate((cs,csn))
            #print(x,y,z,csn)

            print("calculated end point: ", endpoint)
            print("calculated end direction: ", enddir,"\n")
            ax.plot3D(xline, yline, zline, colors[i%len(colors)])

        colorsMap='OrRd' #'autumn'#'seismic'
        cm = plt.get_cmap(colorsMap)
        cNorm = cls.Normalize(vmin=min(cs), vmax=max(cs))
        scalarMap = mpl.cm.ScalarMappable(norm=cNorm, cmap=cm)
        ax.scatter(x, y, z, c=scalarMap.to_rgba(cs))
        scalarMap.set_array(cs)
        fig.colorbar(scalarMap)
    
        plt.show()

    def randVectorFunc(self, prev):
        r = random.random()
        if (r < 0.3):
            return CONST.SINSQR_PLUS_COS
        elif (r < 0.6):
            return CONST.SIN_COS
        else:
            return CONST.TREFOIL