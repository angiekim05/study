# 플로이드 와샬 : 모든 쌍 간의 최단 거리 구하는 알고리즘
# 다익스트라 : 한 노드에서 나머지 모든 노드까지의 최단 거리 구하는 알고리즘

# 노드 v개, 간선 e개
# 공간복잡도: 플로이드(v**2) vs 다익스트라(v+e)
# 시간복잡도: 플로이드(v**3) vs 다익스트라(v log v(우선순위큐))
# 간선 수가 많으면(v**2 == e) 다익스트라보다 플로이드가 빠를 수 있음
# 음의 가중치가 있다면 플로이드 사용 / 다익스트라 불가

import sys
from heapq import heappop,heappush
input = sys.stdin.readline
n,m,r = map(int, input().split())
items = [0] + list(map(int,input().split()))

# 다익스트라
g = [[] for _ in range(n+1)]
# 그래프 정보 입력
for _ in range(r):
    a,b,l = map(int, input().split())
    # 양방향 간선
    g[a].append((b,l))
    g[b].append((a,l))

dist = [[float("inf")] * (n+1) for _ in range(n+1)]

def dijkstra(start):
    q = [(0,start)]
    dist[start][start] = 0
    while q:
        d,x = heappop(q)
        if dist[start][x] < d:
            continue
        for nx, nd in g[x]:
            next_dist = d + nd
            if dist[start][nx] > next_dist:
                dist[start][nx] = next_dist
                heappush(q,(dist[start][nx],nx))
    item_cnt = 0
    for i in range(1,n+1):
        if dist[start][i] <= m:
            item_cnt += items[i]
    return item_cnt

max_numb = 0
for i in range(1,n+1):
    s = dijkstra(i)
    if max_numb < s:
        max_numb = s
print(max_numb)