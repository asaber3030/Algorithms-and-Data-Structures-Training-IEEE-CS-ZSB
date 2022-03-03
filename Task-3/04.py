pos = 0

stones = input()
ins = input()

for i in list(ins):
  if stones[pos] == i:
    pos += 1

print(pos + 1)