from collections import defaultdict
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
n,e = map(int,input().split())
g = defaultdict(list)
for _ in range(e):
    a,b,c = map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))

# 꼭 지나야 하는 정점
v1, v2 = map(int,input().split())

# start에서 end까지의 최단거리를 구하는 방법
def dijkstra(start,end):
    distance = [float("inf")]*(n+1)
    distance[start] = 0
    q = []
    heappush(q,(0,start))
    while q:
        d, node = heappop(q)
        if node == end:
            break
        for next_node, next_d in g[node]:
            # start에서 다음 노드까지의 거리와 
            # start에서 현재 노드까지의 거리에 
            # 다음 노드까지의 거리를 더한 것을 비교하고 
            # 전자보다 후자가 작다면 추가하기
            if d+next_d < distance[next_node]:
                distance[next_node] = d+next_d
                heappush(q,(distance[next_node], next_node))
    return distance[end]

# v1,v2를 지나고 1 에서 N까지 이동하는 방법
# 1 - v1 - v2 - N
ans1 = dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)
# 1 - v2 - v1 - N
ans2 = dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n)
answer = min(ans1,ans2)
if answer < float("inf"):
    print(answer)
else:
    print(-1)