skills = list(map(int, input().split()))[:2]
problems = list(map(int,(input().split())))

n = skills[0]
k = skills[1]

position = 0

c = 0

for i in range(0, n):
  if problems[i] <= k:
    c = c + 1
  elif problems[i] > k:
    position = i + 1
    break

if position > 0 and position < n:
  for i in range(n - 1, position + 1):
    if problems[i] <= k:
      c = c + 1
    elif problems[i] > k:
      break

print(c)
