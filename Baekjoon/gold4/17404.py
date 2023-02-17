import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int,input().split())) for _ in range(n)]

ans = 1000001

for i in range(3):
    dp = [[1001] * 3 for _ in range(n)]
    dp[0][i] = rgb[0][i]
    for j in range(1,n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + rgb[j][0] # 삘간색 0
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + rgb[j][1] # 초록색 1
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + rgb[j][2] # 파란색 2
    dp[-1][i] = 1000001 # 첫번째 집과 같은 색이면 큰 수를 입력하여 최소비용이 안되도록 함
    ans = min(ans,min(dp[-1])) # 최소비용

print(ans)