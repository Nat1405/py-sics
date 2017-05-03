# A script to calculate the path length difference of sound heard with both ears.
# copyright ncomeau
#
# Activate script

import math

# To do: add an actually rigorous speed of sound calculation
speed_of_sound = 340.0

while True:
    distance = float(raw_input("Enter distance from source to center of head: "))
    radius_head = float(raw_input("Enter radius of head in meters: "))
    theta = int(raw_input("Enter integer angle of head rotation in degrees: "))
    psi = (90 - theta)
    psi = math.radians(psi)
    # Begin calculations
    # left and right ear calculation
    alpha = radius_head * math.cos(psi)
    tau = radius_head * math.sin(psi)
    x = math.sqrt(((distance + alpha)**2)+(tau**2))
    y = math.sqrt(((distance - alpha)**2)+(tau**2))

    print("Left ear path length is " + str(x))
    print("Right ear path length is " + str(y))

    # Calculate and print difference in time between two ears
    left_ear_time = x/speed_of_sound
    right_ear_time = y/speed_of_sound
    delta_arrival_time = abs(left_ear_time - right_ear_time)
    print("Delta in arrival time is " + str(delta_arrival_time))
