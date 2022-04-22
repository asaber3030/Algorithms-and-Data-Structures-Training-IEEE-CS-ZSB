def sort(num):
  for j in range(len(num)):
    for i in range(len(num) - j - 1):
      if num[i] > num[i + 1]: num[i], num[i + 1] = num[i + 1], num[i]
  return num


num = input().split()
print("".join((sort(num))[::-1]))
