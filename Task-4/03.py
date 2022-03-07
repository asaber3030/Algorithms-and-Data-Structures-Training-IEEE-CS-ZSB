txt = input()
pos = '/'

print(pos + pos.join(filter(None, txt.split(pos))))