# 플로이드 와샬 : 모든 쌍 간의 최단 거리 구하는 알고리즘
# 다익스트라 : 한 노드에서 나머지 모든 노드까지의 최단 거리 구하는 알고리즘

# 노드 v개, 간선 e개
# 공간복잡도: 플로이드(v**2) vs 다익스트라(v+e)
# 시간복잡도: 플로이드(v**3) vs 다익스트라(v log v(우선순위큐))
# 간선 수가 많으면(v**2 == e) 다익스트라보다 플로이드가 빠를 수 있음
# 음의 가중치가 있다면 플로이드 사용 / 다익스트라 불가

import sys
input = sys.stdin.readline
n,m,r = map(int, input().split())
items = [0] + list(map(int,input().split()))
# item 개수 정보
item_cnt = [[0]*(n+1) for _ in range(n+1)]

# 플로이드 와샬
g = [[float("inf")]*(n+1) for _ in range(n+1)]
# 그래프 정보 입력
for _ in range(r):
    a,b,l = map(int, input().split())
    # 양방향 간선
    g[a][b] = l
    g[b][a] = l

# 플로이드 와샬의 핵심
# i -> j 로 가는 경로는 바로 가는 경우 vs k 노드를 거쳐 가는 경우
# 둘 중 작은 값으로 갱신
# k : 경유지

# 양방향이 아닌 경우
# for k in range(1,n+1):
#     # 자기 자신으로 이동 = 0
#     g[k][k] = 0
#     # i : 출발지
#     for i in range(1,n+1):
#         # j : 도착지
#         for j in range(1,n+1):
#             if g[i][j] > g[i][k]+g[k][j]:
#                 g[i][j] = g[i][k]+g[k][j]
#             if g[i][j] <= m:
#                 item_cnt[i][j] = items[j]

# 양방향인 경우
for k in range(1,n+1):
    # 자기 자신으로 이동 = 0
    g[k][k] = 0
    item_cnt[k][k] = items[k]
    # i : 출발지
    for i in range(1,n+1):
        # j : 도착지
        for j in range(i+1,n+1):
            if g[i][j] > g[i][k]+g[k][j]:
                g[i][j] = g[i][k]+g[k][j]
                g[j][i] = g[i][k]+g[k][j]
            if g[i][j] <= m:
                item_cnt[i][j] = items[j]
                item_cnt[j][i] = items[i]

max_numb = 0
for i in range(1,n+1):
    s = sum(item_cnt[i])
    if max_numb < s:
        max_numb = s
print(max_numb)