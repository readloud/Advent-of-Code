#Instructions: https://adventofcode.com/2018/day/1

with open('codes.txt','r') as f:
  codes = f.read().splitlines()

#Part one:
c = 0
for i in codes:
  c = eval(str(c)+i)
print(f"Answer #1: {c}")

#Part two:
twice = []
c, r = (0, 0)
while r != -1:
  r += 1
  if r % 10 == 0:
    print(f"Attempt #{r}")
  for i in codes:
    c = eval(str(c)+i)
    if c in twice:
      print(f"Answer #2: {c}")
      r = -1
      break
    twice.append(c)
