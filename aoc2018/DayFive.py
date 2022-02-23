#Instructions: https://adventofcode.com/2018/day/5
import time
from string import ascii_lowercase

with open('input.txt','r') as f:
  d = f.read()

data = d
#Part one
start = time.time()
i = 0
while True:
  cD = data
  for c in range(len(data)):
    try:
      if data[c].lower() == data[c+1].lower() and data[c] != data[c+1]:
        data = data[:c]+data[c+2:]
    except:
      continue
  if cD == data:
    break
  i += 1
results = [len(data), i]
end = time.time()

print(f"New length: {results[0]}")
print(f"Found in iteration #{results[1]}, in {end-start} seconds.")


smallest = [0,len(d)]
#Part two
for char in ascii_lowercase:
    print(f"Attempting: {char}")
    data = d.replace(char.upper(),"").replace(char,"")
    while True:
      cD = data
      for c in range(len(data)):
        try:
          if data[c].lower() == data[c+1].lower() and data[c] != data[c+1]:
            data = data[:c]+data[c+2:]
        except:
          continue
      if cD == data: break
    if len(data) < smallest[1]:
        smallest = [char, len(data)-1]

print(f"The smallest possible string is made by removing '{smallest[0]}', and results in {smallest[1]} chars.")
