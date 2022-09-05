a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

if a >= b and a > c :
  print(str(a),"is the greatest.")
elif b > a and b >= c :
  print(str(b),"is the greatest.")
else :
  print(str(c),"is the greatest.")

# result = max(first,max(second,third)) ...... print(result)