infile = "input/day1.txt"
from collections import defaultdict

elfCal = defaultdict(lambda: 0)

with open(infile,'r') as f:
    i=1
    for line in f.readlines():
        if line.isspace():
            i+=1
            continue
        elfCal[i]+=int(line)

print("Part 1: "+str(max(elfCal.values())))

top3 = sorted(elfCal.values())[-3:]

print("Part 2: "+str(sum(top3)))