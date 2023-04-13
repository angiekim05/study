from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(x):
    weight = [0]*(n+1)
    q = [(0,x)]
    while q:
        w,x = heappop(q)
        if x == y:
            print(-w)
            break
        if weight[x] > -w:
            continue
        for nx,nw in bridge[x]:
            if w == 0: # 처음 0일 때, 다음으로 넘어가기 위한 코드
                weight[nx] = nw
                heappush(q,(-weight[nx],nx))
            # 각각 연결된 다리 두 개가 만약 2, 3 중량을 견딘다면
            # 결국 2 중량만 감당할 수 있다. 즉 각각 비교해봐야함
            elif weight[nx] < -w and weight[nx] < nw:
                weight[nx] = min(-w,nw)
                heappush(q,(-weight[nx],nx))

n,m = map(int,input().split())
bridge = defaultdict(list)
for i in range(m):
    a,b,c = map(int, input().split())
    bridge[a].append((b, c))
    bridge[b].append((a, c))

for i in bridge.keys():
    bridge[i].sort(reverse=True)
x,y = map(int,input().split())
dijkstra(x)

#--------------------------------------------------------------------
# 다익스트라 방식도 통과가 되지만 무척 느림
# 분리집합을 사용함으로써 더 빠르게 가능

import sys
input = sys.stdin.readline

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x

n,m = map(int,input().split())
parents = [i for i in range(n+1)]
# q 에 모든 다리가 감당하는 중량을 담음
s = []
for i in range(m):
    a,b,c = map(int, input().split())
    s.append((c,a,b))
x,y = map(int,input().split())

# 가장 무거운 것부터 뽑음 뒤로 갈수록 적은 중량
s.sort(reverse=True)
for w,a,b in s:
    # a,b를 다리로 연결했으니 union으로 parents 통일 -> 연결을 의미
    union(a,b)
    # 만약 시작 x와 끝 y 가 연결되었다면 parents가 같을 것을 활용
    if find(x) == find(y):
        print(w)
        break
