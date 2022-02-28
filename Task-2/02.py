n = int(input())
elements = list(map(int, input().split()))
sec = len(set(elements))
if 0 in elements:
  sec = sec - 1;
print(sec)
