a, b = [int(i) for i in input().split()]
while (b):
  a, b = b, a % b

print("Great Common Divider is " + str(a))
