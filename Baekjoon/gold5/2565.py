# 교차하지 않게 하기 위해 없애야하는 전깃줄의 최소 개수
#    |  0  |  1  |  2  |  3  |  4
#-----------------------------------
# 0. |  -  |  x  |  o  |  o  |  o
# 1. |  x  |  -  |  x  |  x  |  x
# 2. |  o  |  x  |  -  |  o  |  o
# 3. |  o  |  x  |  o  |  -  |  x
# 4. |  o  |  x  |  o  |  x  |  - 

from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
wire = [tuple(map(int,input().split())) for _ in range(n)]
wire.sort()
dp = [0]*n
for i in range(n):
    for j in range(i+1, n):
        # i번째 전깃줄의 B전봇대 연결 위치가 
        # j번째보다 더 낮으면 (숫자가 더 크면) 교차!
        if wire[i][1] > wire[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
dp[i] += 1
print(n - max(dp))