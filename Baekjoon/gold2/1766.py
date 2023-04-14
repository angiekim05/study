from heapq import heappop, heappush
from collections import defaultdict
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
in_ = [0]*(n+1) # 진입차수
tree = defaultdict(list) # 트리
for i in range(m):
    a,b = map(int, input().split())
    tree[a].append(b)
    in_[b] += 1 # 진입차수 증가

# 진입차수가 0인 시작 노드들을 q에 담음
q = []
for i in range(1,n+1):
    if in_[i] == 0:
        heappush(q,i)

ans = []
while q:
    # q에 담긴 애들 중 가장 작은 문제부터 풀어야 함
    x = heappop(q)
    ans.append(x)

    for nx in tree[x]:
        # 진입차수를 감소시키고 0이 되면 q에 넣어줌
        in_[nx] -= 1         
        if in_[nx] == 0:
            heappush(q,nx)

print(*ans)
