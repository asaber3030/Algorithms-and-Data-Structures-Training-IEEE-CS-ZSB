line = list(map(int, input().split(" ")))
n = line[0]
p = line[1]
k = line[2]

output = [f"({p})"]

def inline(w):
  print(w, end=' ')

if p != 1:
  inline("<< ")

for i in range(1, k + 1):

  if p - i >= 1:
    output.insert(0, p - i)
  if p + i <= n:
    output.append(p + i)

print(*output, end='')

if p != n:
  inline(" >>")

