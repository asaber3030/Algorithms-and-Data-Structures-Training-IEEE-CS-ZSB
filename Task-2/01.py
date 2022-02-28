matrix = []

for n in range(0, 5):
  matrix.append(list(map(int, input().split())))

steps = 0

for i in range(0, len(matrix)):
  for j in range(0, len(matrix)):

    if matrix[3][3] == 1:
      steps = 0
    elif matrix[i][j] == 1:
      steps = abs(j - 2)

  if 1 in matrix[i]:
    steps += abs(i - 2)

print(steps)