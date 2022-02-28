n = list(map(int, input().split())) # n*m matrix

pixels = []

color = 0

for i in range(0, n[0]):
  pixels.append(list(input().split()))

for i in pixels:
  if 'M' in i or 'C' in i or 'Y' in i:
    color = 1
    break

if color == 1:
  print("#Color")
else:
  print("#Black&White")