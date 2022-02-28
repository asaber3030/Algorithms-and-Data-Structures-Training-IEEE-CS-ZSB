n = int(input())
arr = list(map(int, input().split()))[0:n]
m = int(input())

for i in range(0, m):
  v = list(map(int, input().split()))[0:2]

  x = v[0]
  y = v[1]

  right = arr[x - 1] - y
  left = y - 1

  if x - 1 >= 1:
    arr[x - 2] += left

  if x + 1 <= n:
    arr[x] += right

  arr[x-1] = 0


print(*arr)