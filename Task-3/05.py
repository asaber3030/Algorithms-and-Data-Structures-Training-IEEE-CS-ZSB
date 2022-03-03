n = int(input())
s = input()
r = 0
g = 0
b = 0

for i in range(1, n):
  if s[i - 1] == s[i]:
    if s[i] == 'R':
      r = r + 1
    elif s[i] == 'G':
      g = g + 1
    elif s[i] == 'B':
      b = b + 1

print(r + g + b)