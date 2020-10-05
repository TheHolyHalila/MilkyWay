from path import Path
from splines import CubicSpline, NaturalCubicSpline
from vector import Vector2D

spline1 = CubicSpline(Vector2D(0 ,0, 0), Vector2D(1, 1, 0), number_of_points=100)
spline1.get_linear_points()

spline2 = NaturalCubicSpline(Vector2D(0, 0, 0), Vector2D(1, 1, 0), number_of_points=100)
spline2.get_linear_points()

path = Path(spline1,spline2)
path.plot()