n = int(input())

seats = []

answer = False

for i in range(0, n):
  seats.append(input().split("|"))


for i in (0, n - 1):
  for j in range (0, len(seats[i])):
    if seats[i][j] == 'OO':
      seats[i][j] = "++"
      answer = True
      break
  if seats[i][j] == "++":
    break

if answer == True:
  print("YES")
  for i in seats:
    print("|".join(i))
else:
  print("NO")

