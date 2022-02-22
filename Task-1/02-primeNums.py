import math
n = int(input("Number? "))

ns = [n / math.log(n), 1.25506 * (n/math.log(n))]
print(*ns, end=' ')