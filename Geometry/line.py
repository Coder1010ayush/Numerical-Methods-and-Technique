"""

    this class will deals with line and
    related to its properties and functions
    this class will be prioritized in any condition

"""
import sys
import os
sys.path.insert(0, '/home/endless/Documents/Mathematics/venv/script/error')
sys.path.insert(0, '/home/endless/Documents/Mathematics/venv/script/LinearAlgebra')
from error_handling import  ErrorHandler
from matrix import Matrix
from point import Point
import math

class Line(ErrorHandler):

    def __init__(self,a=1,b=1,c=0):
        super().__init__()
        self.x_attr = a
        self.y_attr = b
        self.constant = c

    def __str__(self):
        
        sign1 = "+"
        var1 = 1

        sign2 = "+"
        var2 = 1

        sign = 1
        var = 1

        if self.y_attr<0 :
            sign1 = "-"
            var1 = -1

        if self.constant<0:
            sign2 = "-"
            var2 = -1
        if self.x_attr<0:

            sign = "-"
            var = -1

        str = f"{self.x_attr}x {sign1} {var1*self.y_attr}y {sign2} {var2*self.constant} = 0"
        return  str

    def slope(self):

        if self.x_attr==0.0:
            print( f'slope is infinity')
            return
        slope = (-1*self.y_attr)/self.x_attr
        return slope


    def distance_point_line(self,point):

        x1 = point.x_cord
        y1 = point.y_cord

        mod_dist = abs(self.x_attr*x1 + self.y_attr*y1 + self.constant)
        mod_act = (self.x_attr**2 + self.y_attr**2)**0.5
        if mod_act==0.0:
            raise ValueError("there must be a valid line.")
        dist = mod_dist/mod_act
        return dist

    def isPointOnLine(self,point):

        d = self.distance_point_line(point)
        if d == 0.0:
            return True
        else:
            return False

    def parallel_line_dist(self,other):

        ratio = self.x_attr/other.x_attr
        other.x_attr = other.x_attr*ratio
        other.y_attr = other.y_attr*ratio
        other.constant = other.constant * ratio
        f1 = abs(other.constant-self.constant)
        f2 = (other.x_attr**2 + other.y_attr**2)**0.5
        return f1/f2



    def distance_line_line(self,other):

        if self.isParrallel(other):
            dist = self.parallel_line_dist(other)
            return dist

        else:
            return 0.0


    def isParrallel(self,other):
        a1 = self.x_attr
        a2 = other.x_attr
        b1 = self.y_attr
        b2 = self.y_attr
        if a1/a2 == b1/b2:
            return True
        else:
            return False

    def isIntersecting(self,other):
        
        # check for parallel line condition
        if self.x_attr/other.x_attr == self.y_attr == other.y_attr:
            return False
        else :
            return True

    def findAngle(self,other):

        tan_theta = 0
        f1 = self.x_attr*other.y_attr - self.y_attr*other.x_attr
        f2 = self.x_attr*other.x_attr + self.y_attr*other.y_attr
        tan_theta = abs(f1/f2)
        angle = math.atan(tan_theta)
        return angle

    def isPerpendicular(self,l2):
        slop1 = self.slope()
        slop2 = l2.slope()
        if slop1*slop2 == -1:
            return True
        else:
            return False


    def check_cuncurrency(*args):
        if len(args) >=3:
            line1 = args[0]
            line2 = args[1]
            line3 = args[2]
            a1 = line1.x_attr
            a2 = line2.x_attr
            a3 = line3.x_attr

            b1 = line1.y_attr
            b2 = line2.y_attr
            b3 = line3.y_attr

            c1 = line1.constant
            c2 = line2.constant
            c3 = line3.constant
            mat = [[a1,b1,c1],[a2,b2,c2],[a3,b3,c3]]
            det = Matrix.determinant(mat)
            if det == 0.0:
                return True
            else: 
                return False


        else: 
            raise Exception("for checking cuncurrency , there must be 3 lines given.")

if __name__ == '__main__':
    l1 = Line(1,1,0)
    print('slope is ' , l1.slope())
    print('equation of line is ',l1)
    mat = [
        [1,2,3],
        [3,4,5],
        [5,2,0]
    ]
    


