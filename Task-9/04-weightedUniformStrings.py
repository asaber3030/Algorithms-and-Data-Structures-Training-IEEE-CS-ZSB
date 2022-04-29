import string
letters = string.ascii_lowercase

def weightedUniformStrings(s, queries):
  result = []
  d = {}
  weight = 0

  for i in range(len(s)):
    if i == 0 or s[i] != s[i - 1]:
      weight = ord(s[i]) - ord('a') + 1
    else:
      weight = weight + ord(s[i]) - ord('a') + 1

    d[weight] = 1

  for q in queries:
    if q in d:
      result.append('Yes')
    else:
      result.append('No')

  return result


s = input()

queries_count = int(input().strip())

queries = []

for _ in range(queries_count):
    queries_item = int(input().strip())
    queries.append(queries_item)

result = weightedUniformStrings(s, queries)

print(*result)