import re
import copy

infile = "input/day5.txt"

def extract_crates(lines):
    crates_str = []
    while "[" in lines[0]:
        crates_str.append(lines.pop(0))
    return crates_str

def parse_crates(text:list):
    # line length = 3n + (n-1) = 4n-1
    line_length = len(text[0])
    n_crates = int((line_length + 1)/4)
    crates = [[] for _ in range(n_crates)]
    for i in range(len(text)):
        line = text[len(text)-i-1]
        for j in range(n_crates):
            letter = line[4*j + 1]
            if letter.isspace():
                continue
            crates[j].append(letter)
    return crates

with open(infile,'r') as f:
    contents = f.readlines()
    f.close()

crates = parse_crates(extract_crates(contents))

p = re.compile(r"move (\d+) from (\d+) to (\d+)")
instructions = list(map(lambda line: p.match(line).groups(),contents[2:]))

crates_p1 = copy.deepcopy(crates)
for step in instructions:
    source, target, num = int(step[1])-1, int(step[2])-1, int(step[0])
    for i in range(num):
        crates_p1[target].append(crates_p1[source].pop())

crates_p2 = copy.deepcopy(crates)
for step in instructions:
    source, target, num = int(step[1])-1, int(step[2])-1, int(step[0])
    to_move = crates_p2[source][-1*num:]
    for i in range(num):
        crates_p2[source].pop()
    crates_p2[target]+=to_move

print("".join([row[-1] for row in crates_p1]))
print("".join([row[-1] for row in crates_p2]))