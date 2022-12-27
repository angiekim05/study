# dp를 활용하여 i에서 j까지 행렬곱을 담아 최소값을 구함
# ABCDE연속행렬 곱에 필요한 연산의 최솟값 =
# min(
# min(A) + min(BCDE) + 행렬곱에 필요한 연산수(A행 * A열 * E열),
# min(AB) + min(CDE) + 행렬곱에 필요한 연산수(A행 * B열 * E열),
# min(ABC) + min(DE) + 행렬곱에 필요한 연산수(A행 * C열 * E열),
# min(ABCD) + min(E) + 행렬곱에 필요한 연산수(A행 * D열 * E열)
# )

import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)] # 행렬 크기 담음
dp = [[0]*n for _ in range(n)] # 최소값 담을 dp

for k in range(1, n): # i와 j 사이의 거리, 즉 왼쪽위에서 오른쪽아래로 향하는 대각선을 오른쪽으로 이동하면서 차례로 채우게 됨
    for i in range(n-k): 
        j = i+k 
        dp[i][j] = 2**31 # 초기 값을 최대 값으로 채움
        for mid in range(i, j): # 중간에 거처가는 값을 mid로 두고 연속행렬 곲의 최솟값을 구함
            temp = dp[i][mid] + dp[mid+1][j] + a[i][0]*a[mid][1]*a[j][1] # mid 기준 왼쪽 행렬 최솟값 + 오른쪽 행렬 최솟값 + 두개의 행렬곱에 필요한 연산수
            if dp[i][j] > temp:
                dp[i][j] = temp
print(dp[0][n-1])
