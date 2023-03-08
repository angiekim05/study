import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

dp = [1] * n
b = [[a[i]] for i in range(n)]
for i in range(1,n):
    for j in range(i):
        if a[j] < a[i] and dp[i] < dp[j] + 1: 
            dp[i] = dp[j] + 1
            b[i] = b[j]+[a[i]]
m = max(dp)
print(m)
print(*b[dp.index(m)])