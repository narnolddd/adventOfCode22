import re

infile = "input/day4.txt"

def is_nested(l1,u1,l2,u2):
    if (l1 <= l2) & (u1 >= u2):
        return True
    if (l1 >= l2) & (u1 <= u2):
        return True
    return False

def is_overlapping(l1,u1,l2,u2):
    if (u1 < l2) | (u2 < l1):
        return False
    return True

p = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")

contained_pairs = 0
overlapping_pairs = 0

with open(infile,'r') as f:
    for line in f.readlines():
        w, x, y, z = p.match(line).groups()
        if is_nested(int(w),int(x),int(y),int(z)):
            contained_pairs+=1
        if is_overlapping(int(w),int(x),int(y),int(z)):
            overlapping_pairs+=1

print("Part 1: "+str(contained_pairs))
print("Part 2: "+str(overlapping_pairs))