import sys
input = sys.stdin.readline
n = int(input())
candy = [list(input().strip()) for _ in range(n)]

# 자리 바꾸면 총 3출의 가장 긴 연속 행 or 열을 확인하면됨
def check_candy(x,y,nx,ny):
    max_cnt = 0
    if ny == y: # row2개 col1개
        r1,r2,c1 = 1,1,1
        for i in range(1,n):
            if candy[x][i-1] == candy[x][i]:
                r1 += 1
            else:
                r1 = 1
            if candy[nx][i-1] == candy[nx][i]:
                r2 += 1
            else:
                r2 = 1
            if candy[i-1][y] == candy[i][y]:
                c1 += 1
            else:
                c1 = 1
            max_cnt = max(max_cnt,r1,r2,c1)
            
    else: # row1개 col2개
        r1,c1,c2 = 1,1,1
        for i in range(1,n):
            if candy[x][i-1] == candy[x][i]:
                r1 += 1
            else:
                r1 = 1
            if candy[i-1][y] == candy[i][y]:
                c1 += 1
            else:
                c1 = 1
            if candy[i-1][ny] == candy[i][ny]:
                c2 += 1
            else:
                c2 = 1
            max_cnt = max(max_cnt,r1,c1,c2)
    return max_cnt


# 최대 사탕 개수를 담을 변수   
max_cnt = 0
dx,dy = (1,0), (0,1) # 아래 & 오른쪽만 확인해도 됨.
for i in range(n):
    for j in range(n):
        for k in range(2):
            nx, ny = i+dx[k], j+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: # 바깥으로 넘어가면 패스
                continue
            # 현재 색깔과 다음 색깔 바꾸기
            candy[i][j],candy[nx][ny] = candy[nx][ny],candy[i][j]            
            max_cnt = max(max_cnt,check_candy(i,j,nx,ny))
            # 원상복귀
            candy[i][j],candy[nx][ny] = candy[nx][ny],candy[i][j]
print(max_cnt)

# 힌트 봄
# 문제가 짧다고 바로 풀기 넘어가다가 "가장 긴 연속 부분" 놓침.. 
# 문제 꼼꼼히 읽기! 심플하게 생각해보기!