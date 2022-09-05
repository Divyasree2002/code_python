import math
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
 
sqroot = math.sqrt(a)    # a ** 2
cube = b ** 3 
cuberoot = c ** (1/3)

print(sqroot,"is the square root of ", a )
print(cube, "is the cube of ", b )
print(cuberoot, "is the cube of", c )
