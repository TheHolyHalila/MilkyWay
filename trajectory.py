'''
Generic Trajectory abstract class

Not to be confused with Motion planned trajectories ('Trajectory' is only for naming)

Author: Hali Lev Ari
Version: 1.0
'''

from abc import ABC, abstractmethod
from vector import Vector2D
import numpy as np

class Trajectory(ABC):
    """
    Trajectory
    ==========

    Description:
    ---
        Describes the basic functionality a trajectory type should have.
        Has a group of basic functions that the trajectories should implement.
        Path between 2 points.

        Inherited classes may raise NotImplementedError

    ToDo:
    -----
        Maybe add adaptive sampling based on curvature
        Concider a more generic parent class 'Trajectory' and make this one 'DiscreteTrajectory' and make a subclass 'ParametricTrajectory'
    """
    
    def __init__(self) -> None:

        # Making aliases
        self.linear = self.get_linear_points
        self.equidistant = self.get_equidistant_points

    @abstractmethod
    def create_trajectory(self, V1: Vector2D, V2: Vector2D, k:int=1, number_of_points:int=10) -> bool:
        """
        create_trajectory
        =================

        Description:
        ------------
            Changes the object trajectory starting and finising point

        Arguments:
        ----------
            V1: The first point of the trajectory
            V2: The last point of the trajectory
            k:  Curvature (defaults to 1)

        Returns:
        --------
            Whether the points are valid

        Raises:
        -------
        ValueError
            If V1 and V2 are on the same x,y

        """
        raise NotImplementedError

    @abstractmethod
    def get_linear_points(self, amount_of_point:int) -> np.ndarray:
        """
        get_linear_points
        =================

        Description:
        ------------
            Creates a numpy array of Vector2D consists of linearly picked points

        Notes:
        ------
            Samples may vari in length and may not have consistant distance

        Arguments:
        ----------
            amount_of_points: The amount of points to return

        Returns:
        --------
            Vector2D array

        rtype:
        ------
            np.ndarray
        """
        raise NotImplementedError

    @abstractmethod
    def get_equidistant_points(self, amount_of_points: int) -> np.ndarray:
        """
        get_equidistant_points
        =================

        Description:
        ------------
            Creates a numpy array of Vector2D consists of equidistant points (May implement the get_linear_points)

        Arguments:
        ----------
            amount_of_points: The amount of points to return

        Returns:
        --------
            Vector2D array

        rtype:
        ------
            np.ndarray
        """
        raise NotImplementedError
