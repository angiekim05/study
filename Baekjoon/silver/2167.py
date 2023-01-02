# 배열이 주어지고 k개의 (i,j),(x,y) 구간의 부분 합을 구하는 문제
# 누적합을 통해 부분합을 쉽게 구할 수 있음

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 누적합 구하기
s = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        s[i][j] = arr[i-1][j-1] + s[i-1][j] + s[i][j-1] - s[i-1][j-1]

# 부분합 구하기
k = int(input())
for _ in range(k):
    i,j,x,y = map(int,input().split())
    ans = s[x][y] - s[i-1][y] - s[x][j-1] + s[i-1][j-1]
    print(ans)