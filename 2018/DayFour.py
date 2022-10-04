#Instructions: https://adventofcode.com/2018/day/4
from collections import defaultdict

with open('codes.txt','r') as f:
  codes = f.read()
  codes = codes.splitlines()
  codes.sort()

guards = defaultdict(lambda: {str(i).zfill(4):0 for i in [j for j in range(0000,60)]})

times = []
for count, code in enumerate(codes):
  time = int(code[12:17].split(":")[1])
  times.append(time)
  if code.split(" ")[3][0] == "#":
      currentGuardNo = code.split(" ")[3]
  if "wakes" in code and "falls" in codes[count-1]:
      for i in range(times[count-1], time):
        guards[currentGuardNo][str(i).zfill(4)] += 1

#Guard name1, most freq minute, total mins asleep, Guard name2, most freq min asleep
mostMins = [0,0,0,0,0,0]
for guard in guards:
    guardTimes = guards[guard]
    biggest = max(guardTimes, key=guardTimes.get)
    total = sum([n for n in guardTimes.values()])
    if total > mostMins[2]:
      mostMins = [guard, biggest, total]+mostMins[3:]
    if guardTimes[biggest] > mostMins[4]:
      mostMins = mostMins[:3]+[guard, guardTimes[biggest], biggest]

print("Guard %s slept the most (%d minutes)." % (mostMins[0], mostMins[2]))
print("Their most frequent minute to sleep was %s." % mostMins[1])
print("The flag for part one is (%s * %s) %d." % (mostMins[0][1:], mostMins[1], int(mostMins[0][1:])*int(mostMins[1])))

print("Guard %s was most frequently asleep on the same minute (%s)." % (mostMins[3], mostMins[-1]))
print("The flag for part two is (%s * %s) %d." % (mostMins[3][1:], mostMins[-1], int(mostMins[3][1:])*int(mostMins[-1])))
