rows = int(input("Enter number of rows : "))
columns = int(input("Enter number of columns : "))

matrix = []
print("Enter the elements : ")
for i in range(rows) :
  a = []
  for j in range(columns) :
    a.append(int(input()))
  matrix.append(a)

for i in range(rows) :
  for j in range(columns) :
    print(matrix[i][j], end = " ")
  print()