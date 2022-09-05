base = float(input("Enter a base value : "))
expo = int(input("Enter a exponential value : "))
result = 1
for expo in range(expo, 0, -1) : 
  result *= base
print(result)

#pow(base,expo)
#result = base ** expo