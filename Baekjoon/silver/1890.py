import sys
input = sys.stdin.readline

n = int(input())
board = [input().split() for _ in range(n)]
m = len(board[0])
dp = [[0]*m for _ in range(n)]
dp[0][0]=1
def sol():
    for i in range(n):
        for j in range(m):
            k = int(board[i][j])
            if k == 0:
                continue
            if i+k < n: 
                dp[i+k][j] += dp[i][j]
            if j+k < m:
                dp[i][j+k] += dp[i][j]
    return dp[-1][-1]
print(sol())
