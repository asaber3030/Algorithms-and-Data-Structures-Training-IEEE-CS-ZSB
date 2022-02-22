distance = int(input("distance?: "))
points = 0

if distance <= 800:
    points += 1

elif 800 < distance <= 1400:
    points += 2

elif 1400 < distance <= 2000:
    points += 3

print(points)