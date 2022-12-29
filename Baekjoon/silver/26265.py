from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
pair = defaultdict(list)
for _ in range(n):
    a,b = input().split()
    pair[a].append(b)
for x in sorted(pair.keys()):
    pair[x].sort(reverse=True)
    for y in pair[x]:
        print(x,y)