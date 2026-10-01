import geometry
from geometry.flat import triangle_area
from  geometry.solid import sphere_volume
from  geometry.solid import hemisphere_area

print("geometry.__version__     =", geometry.__version__)
print("geometry.circle_area(3)  =", round(geometry.circle_area(3), 4))
print("triangle_area(6, 4)      =", triangle_area(6, 4))
print("sphere_volume(3)         =", round(sphere_volume(3), 4))
print("geometry.__all__         =", geometry.__all__)
print("geometry.__file__         =", geometry.__file__)
