import sys
input = sys.stdin.readline
n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]
dp = [10001] * (k+1)
for i in coins:
    if i > k:
        continue
    dp[i] = 1
    for j in range(i+1,k+1):
        dp[j] = min(dp[j], dp[j-i]+1)
if dp[-1] != 10001:
    print(dp[-1])
else:
    print(-1)