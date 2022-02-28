n = int(input()) # number of cards
r = n - 1
l = 0

NOC = list(map(int, input().split())) # Numbers On Cards [NOC]

dScore = 0
sScore = 0

for i in range(0, n):
  if i % 2 == 0:
    if NOC[r] > NOC[l]:
      sScore += NOC[r]
      r = r - 1
    elif NOC[r] < NOC[l]:
      sScore += NOC[l]
      l = l + 1
    else:
      sScore += NOC[l]
  else:
    if NOC[r] > NOC[l]:
      dScore += NOC[r]
      r = r - 1
    elif NOC[r] < NOC[l]:
      dScore += NOC[l]
      l = l + 1
    else:
      dScore += NOC[l]

print(sScore, dScore, end=' ')