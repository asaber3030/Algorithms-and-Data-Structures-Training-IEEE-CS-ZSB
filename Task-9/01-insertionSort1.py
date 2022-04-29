nums = list(map(int, input().split(' ')))
n = len(nums)

def insertionSort(nums, n):
  target = nums[-1]
  i = n - 2
  while target < nums[i] and i >= 0:
    nums[i + 1] = nums[i]
    i -= 1

  nums[i + 1] = target

  return nums

print(insertionSort(nums, n))