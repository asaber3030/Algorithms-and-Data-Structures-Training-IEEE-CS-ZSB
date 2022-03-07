txt = input()
a = txt.find("+")
b = txt.find("=") - a - 1
c = len(txt) - b - a - 2
#
# print(a)
# print(b)
# print(c)

def inline(word):
  print(word, end='')

if a + b == c:
  print(txt)

elif a + b + 1 == c - 1:
  for i in range(0, a + 1):
    inline("|")
  inline("+")

  for i in range(0, b):
    inline("|")
  inline("=")

  for i in range(0, c - 1):
    inline("|")

elif a > 1 and a - 1 + b == c + 1:
  for i in range(0, a - 1):
    inline("|")
  inline("+")

  for i in range(0, b):
    inline("|")
  inline("=")

  for i in range(0, c + 1):
    inline("|")

elif b > 1 and a + b - 1 == c + 1:
  for i in range(0, a):
    inline("|")
  inline("+")

  for i in range(0, b - 1):
    inline("|")
  inline("=")

  for i in range(0, c + 1):
    inline("|")
else:
  print("Impossible")