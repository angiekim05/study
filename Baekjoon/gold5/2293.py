import sys
input = sys.stdin.readline
n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1
# 순차적으로 코인이 사용되어 만들 수 있는 경우의 수
for i in coins:
    for j in range(i,k+1):
        if j - i >= 0:
            dp[j] += dp[j-i]
print(dp[-1])