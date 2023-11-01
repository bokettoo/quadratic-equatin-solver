import math

print("this program solve second degree equation ")
a= int(input("enter the first coefficient"))
b= int(input("enter the second coefficient"))
c= int(input("enter the third coefficient"))


discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / 2 * a
    x2 = (-b - math.sqrt(discriminant)) / 2 * a
    print (x1,x2)
elif discriminant == 0:
   print (-b / 2 * a, -b / 2 * a)
else:
    print("no solution")