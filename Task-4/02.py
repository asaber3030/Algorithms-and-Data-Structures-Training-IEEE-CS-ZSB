a = input()
b = input()

res = None

for i in range(len(a) - 1, -1, -1):
  c = list(a)
  if c[i] != 'z':
    nx = ord(c[i])
    c[i] = chr(nx + 1)

    res = ''.join(c)

  c[i] = 'a'

if res != b:
  print(res)
else:
  print("No")