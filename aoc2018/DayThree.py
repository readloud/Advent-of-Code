#Instructions: https://adventofcode.com/2018/day/3
grid = [[0 for j in range(1000)] for i in range(1000)]

with open('codes.txt','r') as f:
  codes = f.read().splitlines()

positions = [i.split(" ")[2][:-1].split(",") for i in codes]
sizes = [i.split(" ")[-1].split("x") for i in codes]


#Part one
for i in range(len(codes)):
  pos = (int(positions[i][0]), int(positions[i][1]))
  size = (int(sizes[i][0]), int(sizes[i][1]))
  for y in range(pos[1], pos[1]+size[1]):
    for x in range(pos[0], pos[0]+size[0]):
      grid[x][y] += 1

print(len([i for j in grid for i in j if i > 1]))


#Part two
for i in range(len(codes)):
  pos = (int(positions[i][0]), int(positions[i][1]))
  size = (int(sizes[i][0]), int(sizes[i][1]))
  ones = 0
  for y in range(pos[1], pos[1]+size[1]):
    for x in range(pos[0], pos[0]+size[0]):
      if grid[x][y] == 1:
        ones += 1
  if ones == (size[0]*size[1]):
    print(i+1)
    break
