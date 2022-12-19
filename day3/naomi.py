infile = "input/day3.txt"

priority = dict(zip(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"),range(1,53)))

rucksacks = []

priority_tot = 0
with open(infile,'r') as f:
    for line in map(lambda x: x.strip(), f.readlines()):
        rucksacks.append(line)
        pointer = int(len(line)/2)
        wd1, wd2 = set(line[:pointer]), set(line[pointer:])
        common = (wd1.intersection(wd2)).pop()
        priority_tot += priority[common]
        
print("Part 1: "+str(priority_tot))

from itertools import * 

def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')

priority_tot = 0
for sacks in grouper(rucksacks,3):
    common = set(sacks[0])
    for i in range(1,3):
        common.intersection_update(set(sacks[i]))
    priority_tot += priority[common.pop()]

print("Part 2: "+str(priority_tot))