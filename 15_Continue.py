a, b = input("Enter the numbers : ").split()

for i in range(int(a), int(b) + 1) :
  if i % 5 == 0 :
    continue
  print(i ,end = " ")