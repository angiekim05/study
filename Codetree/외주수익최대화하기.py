# https://www.codetree.ai/training-field/frequent-problems/problems/max-of-outsourcing-profit?&utm_source=clipboard&utm_medium=text

# 휴가 기간
n = int(input())

# 날짜별 외주 작업 기한, 수익
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0]*(n+1)
max_ = 0

for i in range(n):
    x, m = arr[i]
    dp[i+1] = max(dp[i+1], dp[i])
    if i+x <= n:
        dp[i+x] = max(dp[i+x], dp[i]+m)
    
print(max(dp))
