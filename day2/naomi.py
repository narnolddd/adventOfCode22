infile = "input/day2.txt"

# win = 1 modulo 3
# draw = 0 modulo 3
# lose = -1 modulo 3

rpsMap = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}
games = []

p1_outcome = 0
with open(infile,'r') as f:
    for line in f.readlines():
        row = line.strip().split(" ")
        x, y = rpsMap[row[0]], rpsMap[row[1]]
        games.append((x,y))
        p1_outcome += y + 3*((y+1-x)%3)

print("Part 1: "+str(p1_outcome))

p2_outcome=0
for game in games:
    x, y = game[0], game[1]
    p2_outcome += (y-1)*3 + (x+y)%3 + 1

print("Part 2: "+str(p2_outcome))