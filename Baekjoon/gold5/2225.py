# 0~n까지의 정수를 k개 더해서 합이 n이 되는 경우의 수
# 중복이 허용되고 순서가 다른 경우도 포함됨으로 중복순열
# python에서 중복순열 함수 활용 -> 시간 초과 => dp 사용
# from itertools import product 
# cnt = 0 
# for case in product(range(n+1),repeat=k):
#     if sum(case) == n:
#         cnt += 1
# 중복순열의 합이 n을 만족하는 경우의 수를 나열해보면
#         0 | 1 | 2 | 3 | 4 
# k = 1,  1 | 1 | 1 | 1 | 1
# k = 2,  1 | 2 | 3 | 4 | 5
# k = 3,  1 | 3 | 6 | 10| 15
# 즉, dp[i][j] = dp[i][j-1] + dp[i-1][j]
# => k번 반복하며 dp를 0에서부터 n까지 누적하면 
#    k개의 정수들의 합이 n이 되는 경우의 수가 나옴

n,k = map(int, input().split())
dp = [0]*(n+1)
dp[0] = 1
for _ in range(k):
    for i in range(1,n+1):
        dp[i] = (dp[i] + dp[i-1])%(10**9)

print(dp[n])