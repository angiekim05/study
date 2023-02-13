n = int(input())
p = list(map(int,input().split()))
m = int(input())
dp = [0]*n
min_ = 50
for i in range(n-1,0,-1):
    if min_ > p[i]:
        min_ = p[i]
        idx = i
if p[0] < min_:
    if min_ <= m:
        m -= min_
        dp[idx] += 1
        while m >= p[0]:
            m -= p[0]
            dp[0] += 1
    else:
        while m >= p[0]:
            m -= p[0]
            dp[0] += 1 
else:
    while m >= min_:
        m -= min_
        dp[idx] += 1
if m > 0:
    for i in range(n-1,0,-1):
        while dp[idx] and idx < i and m + min_ >= p[i]:
            m -= p[i] - min_
            dp[idx] -= 1
            dp[i] += 1
        while dp[0] and m + p[0] >= p[i]:
            m -= p[i] - p[0]
            dp[0] -= 1
            dp[i] += 1
ans = ""
for i in range(n-1,-1,-1):
    while dp[i]:
        dp[i] -= 1
        ans += str(i)
print(int(ans))