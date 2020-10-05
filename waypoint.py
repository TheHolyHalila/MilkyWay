from vector import Vector2D
from math import sqrt

class Waypoint2D(Vector2D):
    '''
    Waypoint2D
    ========
    Implements a waypoint (x,y,theta,curvature)
    
    #Todo:
        Add 'get_angular'- good question
    '''

    def __init__(self, x:float, y:float, theta:float, curvature:float) -> None:
        super().__init__(x, y, theta)
        self.curvature = curvature

    def get_distance(self, other:Vector2D):
        ''' 
        get_distance
        ============
        Returns the euclidean distance between this waypoint and another
        -----------------
        '''
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def get_point(self):
        return self.x, self.y

    def __repr__(self) -> str:
        return 'x: {}, y: {}, theta: {}, curvature: {}'.format(self.x, self.y, self.theta, self.curvature)
    