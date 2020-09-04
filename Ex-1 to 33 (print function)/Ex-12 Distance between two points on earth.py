from math import sin, cos, acos, radians

t1 = radians(float(input("Enter the latitude of first point of earth : ")))
g1 = radians(float(input("Enter the longitude of first point of earth : ")))

t2 = radians(float(input("Enter the latitude of second point of earth : ")))
g2 = radians(float(input("Enter the longitude of second point of earth : ")))

distance = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))

print("Distance between two points on earth is ", "{:.2f}".format(distance))