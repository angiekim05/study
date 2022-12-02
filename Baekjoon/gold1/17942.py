# 각각의 문제를 풀 때 필요한 공부량이 주어지고 (1 ~ 10**8)
# a 문제를 풀었을 때, b 문제의 공부량을 d 씩 줄여주는 관계에 대한 정보가 주어졌을 때
# m 개의 알고리즘을 공부하기 위해 최소로 필요한 공부량을 구하는 문제
# 그리디 + 우선순위큐 사용
# 순간 순간 가장 적은 공부량을 선택하면서 
# 현재 가지고 있는 공부량과 비교하여 필요한 공부량을 구함
# m개를 풀었다면 멈춤
# 이미 공부한 알고리즘은 다시 공부 안하도록 체크!


from collections import defaultdict
from heapq import heappop, heappush, heapify
import sys
input = sys.stdin.readline
# 총 문제 수 n , 풀 문제 수 m 
n,m = map(int,input().split())
# 각각 문제에 대한 공부량
k = [0]+list(map(int,input().split()))

# a문제를 풀었을 때 공부량이 줄어드는 문제 체크
r = int(input())
g = defaultdict(list)
for i in range(r):
    a,b,d = map(int,input().split())
    g[a].append((b,d))

# 우선순위 큐를 사용하여 매번 가장 적은 공부량을 뽑음
# 우선순위 큐 초기화 
# 제일 처음의 각 문제에 대한 공부량을 기준으로 정렬하며 공부량의 위치를 확인할 수 있도록 담아줌
q = [(Ki,i+1) for i, Ki in enumerate(k[1:])]
heapify(q)
# 최종 필요 공부량
ans = 0
# 이미 푼 문제
visited = set()

while len(visited) < m:
    # 공부량 d, 해당 공부량 위치 x
    d, x = heappop(q)

    # 만약 풀었던 문제라면 지나감
    if x in visited:
        continue

    # 풀 문제라면 앞서 필요했던 공부량과 비교하여 필요 공부량 체크
    ans = max(ans,d)
    # 푼 문제로 체크
    visited.add(x)

    # 해당 문제를 풀면 줄어드는 공부량 업데이트
    for nx, nd in g[x]:
        k[nx] -= nd
        heappush(q,(k[nx],nx))

print(ans)