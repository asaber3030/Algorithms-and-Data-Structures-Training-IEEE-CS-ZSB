import re
reg = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

txt = input()
res = re.fullmatch(reg, txt)

if res:
  print('YES')
else:
  print('NO')