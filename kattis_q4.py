import math

x = int(input())
y = int(input())
z = int(input())

large_area = math.pi * ((x/2) ** 2)

small_area = z * math.pi * ((y/2) ** 2)

if (large_area > small_area):
    print("Neibb")
else:
    print("Jebb")