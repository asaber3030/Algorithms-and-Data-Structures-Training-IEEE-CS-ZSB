n = int(input())
t = input()

a = t.count("A")
d = t.count("D")

if a > d:
  print("Anton")
elif a < d:
  print("Danik")
elif a == d:
  print("Frienship")