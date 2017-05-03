#!/usr/bin/env python

distances = [0.39, 0.723, 1, 1.52, 5.2, 9.5, 19.18, 30, 39.53, 4.243*63241, 1644232200.0, 158099250000.0]

radius = float(raw_input("Enter a radius of the Sun: "))

distance = 0

ratio_au_to_sun = 214

size_earth = 0.009*radius
print("Size of Earth to scale is: " + str(size_earth))

for i in distances:
	distance = i*ratio_au_to_sun*radius
	format(distance, '.2f')
	print(str(distance) + " meters")


