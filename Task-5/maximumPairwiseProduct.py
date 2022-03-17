n = int(input())
nums = []

for i in range(0, n):
  r = int(input())
  nums.append(r)

print(nums)

def max_pairwise_product(nums):
  result = 0
  n = len(nums)
  a = nums[0]
  b = nums[1]

  for i in range(0, n):
    for j in range(i + 1, n):
      if (nums[i] * nums[j]) > (a * b):
        a = nums[i]
        b = nums[j]

  return a * b

result = max_pairwise_product(nums)
print(result)