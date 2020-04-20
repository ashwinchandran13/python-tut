#from sphere import * 1method
import sphere #2method

print("Enter the radius of the sphere: ")
radius = int(input())

#print("The area is " + str(area(radius)))
#print("the volume is " + str(volume(radius)))

print("The area is " + str(sphere.area(radius)))
print("the volume is " + str(sphere.volume(radius)))
