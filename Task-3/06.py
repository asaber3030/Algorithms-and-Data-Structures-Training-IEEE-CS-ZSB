max = 0
n = int(input())
s = ''

for i in range(1, n):
  for j in range(1, n + 1):
    if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
      max = max + 2

print(max)


for i in range(1, n + 1):
  for j in range(1, n + 1):
    if (i%2 == 0 and j%2 == 0) or (i%2 == 1 and j%2 == 1):
      print("C")
    else:
      print(".")
