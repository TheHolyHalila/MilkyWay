'''
Implementation of a path 
We concider path as a group of trajectories (trajectory being between 2 points)

Author: Hali Lev Ari
Version: 1.0
'''

from cubic_spline import Waypoint
from typing import List
from trajectory import Trajectory
import numpy as np


class Path:
    '''
    Path
    ====

    Just a class container for a list of connected trajectories
    with a few extra functions
    ------------
    ToDo:
    ----
        Concider a more generic class to inherit from
    '''
    
    trajectories = np.array([])
    waypoints = np.array([])

    def __init__(self, *args: List[Trajectory]):
        '''
        Stich the Trajectories together

        Arguments:
        ----------
            *args: Orderd list of trajectories
        '''

        for trajectory in args:
            self.stich(trajectory)

        self.planned = False

    def stich(self, trajectory:Trajectory, sample='linear'):
        ''' Adding a trajectory to the list'''
        self.trajectories = np.append(self.trajectories, trajectory)

        if self.planned: # Runtime planning
            self.__sample_and_add(trajectory, sample)

    def build_and_stich(self, TrajectoryObj:Trajectory ,first_vector, last_vector, k=1, number_of_points=10, sample='linear'):
        '''
        build_and_stich
        ================

        Builds a trajectory and sticks it in the trajectory array
        ---------
        Arguments:
        ----------
            TrajectoryObj: An objects that inherits from the Trajectory class (for example: CubicSpline)

        '''

        # Init the trajectory
        new_trajectory = TrajectoryObj(first_vector, last_vector, k=k, number_of_points=number_of_points)

        # Stich it in the array
        self.stich(new_trajectory, sample=sample)

    def plan(self, sample='linear'):
        '''
        plan
        ====
        Going all over inner trajectories and 'planning' them
        --------------

        Arguments:
        -----------
            sample: The type of sampling (linear, equidistant)  (To sample points or not to sample, thats the question)
        '''

        self.planned = True

        # Looping on the trajectories
        for trajectory in self.trajectories:            
            self.__sample_and_add(trajectory, sample)

    def __sample_and_add(self, trajectory, sample):
        ''' Method for sampling a new trajectory and concatenateing it to the waypoint array '''

        # Getting the aliased methods and calling them
        trajectory.__getattr__(sample)()

        # Concatenating the waypoints
        self.samples = np.concatenate(self.samples, trajectory.waypoints)

    def __iter__(self):
        '''
        Yielding the waypoints when useing instance as an iterator

        Example:

        for waypoint in path:
            print(waypoint)

        '''
        yield from self.waypoints

    def __add__(self, trajectory:Trajectory):
        '''
        Addind a trajectory

        Example:
        path += trajectory
        '''

        # Adding the trajectory to the list
        self.stich(trajectory)

    def __getitem__(self,indx:int):
        '''
        Returns the nth waypoint

        Example:
        path[3] #=> the forth waypoint
        '''

        # Returning the nth waypoint
        self.samples[indx]

    def __len__(self):
        '''
        Returning the total amount of waypoints

        Example:
        len(path)
        '''

        # Returning the length of the waypoint array
        return len(self.waypoints)
