from itertools import *
import collections

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)

infile = "input/day6.txt"

with open(infile,'r') as f:
    stream = f.readline()
    f.close()

for i, window in enumerate(sliding_window(stream,4)):
    if len(set(window))==4:
        print(i+4)
        break

for i, window in enumerate(sliding_window(stream,14)):
    if len(set(window))==14:
        print(i+14)
        break