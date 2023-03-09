#!/usr/bin/env python
# Phuong trinh bac 2
import math
# Nhap du lieu tu ban phim
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

# Tinh delta
delta = b**2 - 4*a*c

# Xac dinh nghiem
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print ("Nghiem x1 = %0.3f, x2 = %s" % (x1, x2))
elif delta == 0:
    x = -b / (2*a)
    print ("Phuong trinh co nghiem kep x1 = x2 = %0.3f" % x)
else:
    print ("Phuong trinh vo nghiem")