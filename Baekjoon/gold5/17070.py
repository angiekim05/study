# 방향마다 갈 수 있는 곳이 한정되어 있음 -> 방향에 따라 경우의 수 따로 담음
import sys
input = sys.stdin.readline
n = int(input())
wall = [list(map(int,input().split())) for _ in range(n)]
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
# dp[방향][row][col] 오른쪽0/아래쪽1/대각선2
dp[0][0][1] = 1 # 맨 처음 시작

for j in range(2,n): # 첫번째 줄은 모두 오른쪽으로 이동 가능
    if not wall[0][j]:
        dp[0][0][j] = dp[0][0][j-1]

for i in range(1,n):
    for j in range(2,n): # 오른쪽 방향에서 바로 아래 방향으로 갈 수 없음으로 무조건 3번째 열 미만에는 갈 수 없음
        # 이 칸에 도착할 수 있다면
        if wall[i][j] == 0:
            # 오른쪽 이동으로 왔다면 이전에 오른쪽/대각선으로 도착한 경우의 수를 더해줌
            dp[0][i][j] = dp[0][i][j-1]+dp[2][i][j-1]

            # 아래쪽 이동으로 왔다면 이전에 아래쪽/대각선으로 도착한 경우의 수를 더해줌
            dp[1][i][j] = dp[1][i-1][j]+dp[2][i-1][j]
            
            # 대각선 이동으로 이 칸에 도착할 수 있다면
            if wall[i-1][j] == wall[i][j-1] == 0:
                # 이전칸에 오른쪽/아래쪽/대각선으로 도착한 경우의 수를 더해줌
                dp[2][i][j] = dp[0][i-1][j-1]+dp[1][i-1][j-1]+dp[2][i-1][j-1]

# 마지막칸에 세가지 방향으로 도착 가능한 경우의 수 모두 합해줌
print(dp[0][-1][-1]+dp[1][-1][-1]+dp[2][-1][-1])
