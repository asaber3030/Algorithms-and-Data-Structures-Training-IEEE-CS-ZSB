def insertionSort(l):

  for i in range(1, len(l)):
    k = l[i]
    j = i
    while (j > 0 and l[j - 1] > k):
      l[j] = l[j - 1]
      j -= 1

    l[j] = k

  return l


l = list(map(int, input().split(' ')))

for a in insertionSort(l):
  print(a, end=" ")