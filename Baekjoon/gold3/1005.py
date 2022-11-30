# 위상 정렬와 dp를 활용
# dp에 시간을 담고 위상 정렬을 통해 w까지 이동하면서 시간 업데이트

from collections import defaultdict
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    d = [0]+list(map(int, input().split()))

    indegree = [0] * (n+1)
    g = defaultdict(list)
    for _ in range(k):
        x,y = map(int, input().split())
        g[x].append(y)
        indegree[y] += 1

    w = int(input())

    dp = [0] * (n+1) # 각 idx 노드에 도착하기까지 걸리는 시간 담는 곳
    # 위상 정렬
    stack = [] 
    # 진입차수가 0인 경우 stack 에 추가
    for i in range(1,n+1):
        if indegree[i] == 0: # 진입차수가 0이란 것은 이전 노드가 없다는 것 (시작 노드!)
            stack.append(i) # stack에 시작할 노드들 담기
            dp[i] += d[i] # 시작 시간 담기
    
    while stack:
        x = stack.pop() 

        for nx in g[x]:
            indegree[nx] -= 1 # 진입 했으니깐 진입차수 줄이기
            dp[nx] = max(dp[nx],dp[x]+d[nx]) # 이동하면서 최대 시간 걸리는 경우로 update

            # 진입차수가 0이 되면 이전 노드들을 다 거친 것
            # 다음으로 넘어감
            if indegree[nx] == 0 and nx != w: # w면 도착! 더이상 안가도 됨
                stack.append(nx)

    print(dp[w])