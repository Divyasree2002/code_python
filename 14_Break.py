a, b = input("Enter the numbers : ").split()

for i in range(int(a),int(b)+1) :
  print(i, end = " ")
  if i % 13 == 0 :
    break

#list1 = list(map(int,input("Numbers : ").split()))
# low = list1[0]
# high = list1[1]
# while low <= high :
#   print(low, end= " ")
#   if int(low) % 13 == 0 :
#     break
#   low += 1