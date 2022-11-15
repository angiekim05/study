# 교차하지 않게 하기 위해 없애야하는 전깃줄의 최소 개수
# A 전봇대 기준으로 정렬하고
# B 전봇대 기준으로 LIS(가장 긴 증가하는 수열)을 찾으면
# (다음 전깃줄의 B 전봇대 연결 번호가 더 크면 더 아래 있음으로 뒤로 갈수록 숫자가 더 커지는 LIS) 
# 안 교차하는 전깃줄의 최대 개수(c)를 구할 수 있음
# 전체 개수에서 해당 숫자(c)를 빼주면 최소 제거 전깃줄의 개수를 구할수있음

import sys
input = sys.stdin.readline
n = int(input())
wire = [tuple(map(int,input().split())) for _ in range(n)]
wire.sort() # A 전봇대 기준으로 정렬

# 1로 초기화 => 자기 자신의 원소를 의미하는 1
dp = [1]*n

# LIS
for i in range(1,n):
    for j in range(i):
        if wire[i][1] > wire[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1

# 전체 개수에서 최장 증가 수열 개수를 빼주면 됨
print(n - max(dp))