pairs = int(input())
b = list(map(int, input().split())) # bag
t = [] # table
s = [] # what he saw
result = 0 # maximum number of socks

for sock in b:
  if sock not in t:
    t.append(sock)
    if len(t) > result:
      result = len(t)
  else:
    t.remove(sock)
  if sock not in s:
    s.append(sock)
  if len(s) > pairs:
    break


print(result)
