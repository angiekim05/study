from collections import defaultdict
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
g = defaultdict(list)
for _ in range(n-1):
    a,b,c = map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))

for _ in range(m):
    s,e = map(int,input().split())
    q = [(s,0)]
    visited = [0]*(n+1)
    while q:
        x,d = q.pop()
        if x == e:
            print(d)
            break
        for nx,nd in g[x]:
            if visited[nx]:
                continue
            visited[nx] = d+nd
            q.append((nx,d+nd))