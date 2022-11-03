from collections import defaultdict
from heapq import heappop,heappush
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
bus = defaultdict(list)
for _ in range(m):
    s, e, w = map(int,input().split())
    bus[s].append((e,w))
start, end = map(int, input().split())

# 다익스트라 
costs = [float("inf")] * (n+1)
costs[start] = 0
# 노드의 이전 노드
parent = [0] * (n+1)
q = []
heappush(q,(0,start))
while q:
    cost, node = heappop(q)
    # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우 무시
    if cost > costs[node]:
        continue
    for next_node, w in bus[node]:
        next_cost = cost + w
        if next_cost < costs[next_node]:
            costs[next_node] = next_cost
            parent[next_node] = node
            heappush(q,(next_cost,next_node))
        elif next_cost == costs[next_node] and parent[next_node] > node:
            costs[next_node] = next_cost
            parent[next_node] = node
            heappush(q,(next_cost,next_node))

ans = [end]
temp = end
while temp != start:
    temp = parent[temp]
    ans.append(temp)

print(costs[end])
print(len(ans))
print(*ans[::-1])