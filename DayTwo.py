#Instructions: https://adventofcode.com/2018/day/2
import time
from string import ascii_lowercase as alpha

with open('codes.txt','r') as f:
  codes = f.read().splitlines()


#Part one

twice, thrice = (0, 0)
for code in codes:
  two, three = True, True
  for letter in alpha:
    if code.count(letter) == 2 and two == True:
      twice += 1
      two = False
    elif code.count(letter) == 3 and three == True:
      thrice += 1
      three = False
print(twice*thrice)


#Part two
start = time.time()
final = []
def run():
  for code in codes:
    for hashPos in range(len(code)):
      tCode = list(code)
      tCode[hashPos] = "#"
      tCode = ''.join(tCode)
      if tCode in final:
        print(f"Found: {tCode.replace('#','')}")
        return ""
      final.append(''.join(tCode))
end = time.time()
print(f"Time: {end - start}")
