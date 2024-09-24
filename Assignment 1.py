"""
Author: Kingsley Nguyen
Revision date: Sep 24, 2024
Program: Calculate math
Description: a program used to calculate area of a multiple shape
VARIABLE DICTIONARY:
length (float) = length for a rectangle (User input)
width (float) = width for a rectangle (User input)
rarea (float) = area of a rectangle
radius (float) = radius for a circle (User input)
carea (float) = circle area
height (float) = Heigh for a cylinder (User input)
radius2 (float) = new radius for the cylinder top and bottom (User input)
sarea (float) = surface area for the cylinder
volume (float) = volume of a cylinder
plength (float) = length for the pendulum in meters (User input)
gravity (float) = the acceleration speed of gravity (set to 9.8)
pendulum (float) = find the period of time of a pendulum
"""

import math

# Finding area of a rectangle
# Getting the length for a rectangle
length = float(input("Enter the length of a rectangle: "))
# Getting the width for a rectangle
width = float(input("Enter the width of a rectangle: "))
# Calculate the rectangle area
rarea = length*width
# Print out the area of the rectangle
print("The area of a rectangle with your input is: %.2f unit squared"% rarea)

# Finding area of a circle area
# Ask for te radius
radius = float(input("Enter the radius of a circle: "))
# Calculate circle area
carea = math.pi*(radius**2)
# Print out the result of the circle area
print("The area of the circle with given radius is: %.2f unit squared"% carea)

# Finding surface area and volume of a cylinder
# Ask for the height of cylinder
height = float(input("Enter the height of a cylinder: "))
# New variable for the cylinder radius
radius2 = float(input("Enter a new radius: "))
# Find surface area
sarea = (2*math.pi*radius2*height)+(2*math.pi*(radius2**2))
# Find volume
volume = math.pi*(radius2**2)*height
# Print surface area and volume of the cylinder in 2 decimal point
print("The surface area of a cylinder is: %.2f unit squared and the volume is: %.2f unit cubed"% (sarea,volume))

# Finding a period of a pendulum
# Ask for pendulum length in meter
plength = float(input("Enter the length of a pendulum in meter: "))
# Set gravity speed to default
gravity = 9.8
# Calculate pendulum time
pendulum = 2*math.pi*(math.sqrt(length/gravity))
# Print out the pendulum period of time in seconds
print("The period of a pendulum is: %.2f second"%pendulum)