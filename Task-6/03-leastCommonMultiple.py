a, b = [int(i) for i in input().split()]

def lcm(a, b):
  return (a * b) / (a % b)

print(lcm(a, b))