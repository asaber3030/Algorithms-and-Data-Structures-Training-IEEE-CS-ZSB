words = input().strip()

c = 1

for l in words:
  if ord(l) <= ord('Z'):
    c += 1

print(c)
