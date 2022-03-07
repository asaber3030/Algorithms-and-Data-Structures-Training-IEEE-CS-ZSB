line = input().split(' ')

n = int(line[0])
m = int(line[1])
k = float(line[2]) * 100

skills = dict()

name = ''
ex = 0

for i in range(n):
  l2 = input().split(" ")
  name = l2[0]
  ex = int(l2[1]) * k // 100

  if ex >= 100:
    skills[name] = ex

for i in range(m):
  name = input()
  if name not in skills:
    skills[name] = 0


print(len(skills))

for item in skills.items():
  print(item[0], end='')
  print(' ', end='')
  print(item[1])