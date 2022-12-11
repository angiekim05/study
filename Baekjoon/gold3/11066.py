import sys
input = sys.stdin.readline

def sol():
    n = int(input())
    pages = list(map(int, input().split()))
    sum = [0]*(n+1)
    sum[0] = pages[0]
    for i in range(1,n):
        sum[i] = sum[i-1]+pages[i]

    # min_cost[i][j] 에는 i~j까지 범위에서 최소 비용이 들어감
    min_cost = [[0]*n for _ in range(n)]

    # bottom_up 방식으로 맨 처음엔 두개씩 묶은 것부터 시작함 
    # 즉 jump는 i~j 사이의 떨어진 걸이
    for jump in range(1,n):
        for i in range(n-jump):
            j = i+jump

            # i~j 파일을 합친 임시파일 생성 비용은 sum 부분합을 활용
            # (i,j 둘 다 포함)
            # i~j까지의 합은 sum[j]-sum[i-1]
            cost = sum[j]-sum[i-1]

            # 이전 임시파일 생성 최소 비용
            bf_cost = float("inf")
            for mid in range(i,j):
                bf_cost = min(bf_cost, min_cost[i][mid]+min_cost[mid+1][j])

            # i~j까지의 임시파일 생성 최소 비용
            min_cost[i][j] = bf_cost + cost
            
    return min_cost[0][n-1]

t = int(input())
for _ in range(t):
    print(sol())