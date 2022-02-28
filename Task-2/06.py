count = 0;

n = int(input())

s = list(map(int, input().split()))[:n]

min = s[0];
max = s[0];

for i in range(0, len(s)):
  if i != 0:
    if s[i] <= min:
      min = s[i]
      count += 1
    if s[i] > max:
      max = s[i]
      count += 1


print(count)
