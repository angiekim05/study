import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [0]*m # m으로 나눈 나머지 담는 곳
prefixSum = 0
for i in range(n):
    prefixSum += a[i]
    dp[prefixSum%m] += 1

ans = dp[0] # 나머지가 0이 되는 경우의 수
for i in range(m):
    # 같은 크기의 나머지가 되는 prefixSum을 빼서 
    # 나머지가 0이 되는 조합(nC2)을 구해서 더함 
    ans += dp[i] * (dp[i]-1) // 2
print(ans)