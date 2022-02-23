#Instructions: https://adventofcode.com/2018/day/6

#Generate coords
with open('input.txt','r') as f:
    coords = [[int(j) for j in pair] for pair in [i.split(", ") for i in f.read().splitlines()]]
x = max(coords)[0]+10
y = max(i[1] for i in coords)+10

#Generate Grid
grid = [["_" for j in range(y)] for i in range(x)]
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
for char, pair in enumerate(coords):
  grid[pair[1]][pair[0]] = alpha[char]

partTwo = 0
for r in range(x):
  for c in range(y):
    dists = []
    partTwoTotal = 0
    for pair in coords:
      dist = abs(r-pair[1])+abs(c-pair[0])
      partTwoTotal += dist
      dists.append([dist, pair])
    if partTwoTotal < 10000:
      partTwo += 1
    if [c,r] in coords: continue
    big = min(dists)
    if [i[0] for i in dists].count(big[0]) > 1:
      grid[r][c]  = "."
    else:
      grid[r][c]  = grid[big[1][1]][big[1][0]]

for c in alpha:
  if any(c in i for i in grid[0]+grid[-1]):
    print(f"{c} is on edge.")
    alpha = alpha.replace(c,"")
    continue
  if any(c in i for i in [row[0] for row in grid]+[row[-1] for row in grid]):
    print(f"{c} is on edge.")
    alpha = alpha.replace(c,"")

print(alpha)
gridString = ''.join(i for j in grid for i in j)
alphaNum = {gridString.count(c):c for c in alpha}

print(f"The most frequent letter was {alphaNum[max(alphaNum)]} with {max(alphaNum)} occurences.")
print(f"Flag for part two: {partTwo}.")
