nums = list(map(int, input().split(" ")))[:2]
result = 0
for i in range(0, len(nums) - 1):
  result += nums[i] + nums[i + 1]

print(result)