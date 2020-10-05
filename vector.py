'''
Implements vectors

Author: Hali Lev Ari
Version: 1.0
'''

class Vector2D:
    """
    Vector2D
    ========

    Description:
    ------------

        Implements a generic 2D vector

    ToDo:
    -----
        Check if it needs genertic vector operations (addition, multiplication, ETC....)

    Since:
    -----
        Version: 1.0
    """

    def __init__(self, x:float, y:float, theta:float) -> None:
        '''
        Init
        ====

        Arguments:
        ----------

            x: x coordinate
            y: y coordinate
            theta: The angle of the vector
        '''
        # Initilize the variables
        self.x = x
        self.y = y
        self.theta = theta

    def same_point_as(self, V2):
        '''  '''
        return self.x == V2.x and self.y == V2.y