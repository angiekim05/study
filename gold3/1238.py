import sys
input = sys.stdin.readline
from heapq import heappush,heappop

n,m,x=map(int,input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,t = map(int,input().split())
    #단방향
    g[s].append((e,t))

# 다익스트라 start에서 모든 node까지
def dijkstra(start):
    time = [float("inf")]*(n+1)
    time[start]=0
    q = []
    heappush(q,(0,start))
    while q:
        t,node = heappop(q)
        if time[node] > t:
            break
        for next_node, next_time in g[node]:
            cost = t + next_time
            if time[next_node] > cost:
                time[next_node] = cost
                heappush(q,(cost,next_node))
    return time

# 다익스트라 start에서 end node까지
def dijkstra_to(start,end):
    time = [float("inf")]*(n+1)
    time[start]=0
    q = []
    heappush(q,(0,start))
    while q:
        t,node = heappop(q)
        if node == end:
            break
        for next_node, next_time in g[node]:
            cost = t + next_time
            if time[next_node] > cost:
                time[next_node] = cost
                heappush(q,(cost,next_node))
    return time

# x까지 가는 시간
to_x = dijkstra(x)
to_x[0] = 0
for i in range(n):
    if i+1 == x:
        continue
    # x에서 돌아오는 시간 더해주기
    to_x[i+1]+=dijkstra_to(i+1,x)[x]
print(max(to_x))