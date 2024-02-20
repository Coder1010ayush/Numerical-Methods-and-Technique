"""

    this class defines a custom data type of point which
    will be further used in the subsequence classes

"""
import os 
import sys
sys.path.insert(0, '/home/endless/Documents/Mathematics/venv/script/error')
from error_handling import ErrorHandler
import math

class Point(ErrorHandler):

    def __init__(self,x=0,y=0):
        super().__init__()

        # type checking it is either int or float if none of both than raise an error
        if super().check_data_types(x,y):
            self.x_cord = x
            self.y_cord = y

    def __str__(self):
        str = f"({self.x_cord},{self.y_cord})"
        return  str

    def euclidian_distance(self,other):

        f1 = (other.x_cord-self.x_cord)**2
        f2 = (other.y_cord-self.y_cord)**2
        return (f1+f2)**0.5

    def manhattan_distance(self,other):
        f1 = abs(othe.x_cord-self.x_cord)
        f2 = abs(other.y_cord-self.y_cord)
        return f1+f2

    def absolute_distancce_euclidian(self):
        f1 = self.x_cord**2
        f2 = self.y_cord**2
        return  (f1+f2)**0.5

    def absolute_distance_manhattan(self):
        f1 = abs(self.x_cord)
        f2 = abs(self.y_cord)
        return  abs(f1+f2)

    def elevation_from_origin(self):
        if self.y_cord == 0.0 :
            return 90
        tan_theeta = self.x_cord/self.y_cord
        theta_radian = math.atan(tan_theeta)
        theta = math.floor(theta_radian*57.2958)
        return theta

    def to_polar_coordinate(self):
        angle = self.elevation_from_origin()
        sintheta = math.sin(math.radians(angle))
        costheta = math.cos(math.radians(angle))
        resultant_modulus = round(math.sqrt(self.x_cord*self.x_cord + self.y_cord*self.y_cord),3)
        po =  Point(round (resultant_modulus*costheta),round(resultant_modulus*sintheta))
        return {"angle" : angle, "resultant_modulus":resultant_modulus},po




if __name__ == '__main__':
    print("let us start")
    p1 = Point(1,1)
    p2 = Point(1,0)
    ans,po = p1.to_polar_coordinate()
    print(ans)
    print(po)
