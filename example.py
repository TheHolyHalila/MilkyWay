from waypoint import FlexibleWaypoint
from splines import *

# Creating the spline
spline = FlexibleSpline(FlexibleWaypoint(0, 0, angle=90, number_of_points=100),
                        FlexibleWaypoint(1, 1, angle=90, second_derivative=0,k=2, number_of_points=100), FlexibleWaypoint(2, 0, angle=0))

# Plotting the spline
spline.plot()

# Another example
a = FlexibleWaypoint(0, 0, angle=90, number_of_points=100, k=1)
mid1 = FlexibleWaypoint(0.7, 0.8, number_of_points=100)
b = FlexibleWaypoint(1, 1, number_of_points=100)
mid2 = FlexibleWaypoint(1.5, 1, number_of_points=100)
c = FlexibleWaypoint(2, 0, angle=0, k=2)

spline = FlexibleSpline(a, mid1, b, mid2, c)

spline.plot(scatter=True)
