n = int(input())
n1, n2 = 0, 1
count = 0

while count < n:
  print(n1, end=' ')
  nth = n1 + n2
  n1 = n2
  last = n1
  n2 =  nth
  count += 1


