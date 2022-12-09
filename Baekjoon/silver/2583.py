import sys
input = sys.stdin.readline
def dfs(i,j,m,n,arr):
    s = [(i,j)]
    dx,dy = (0,0,1,-1),(1,-1,0,0)
    cnt = 1
    arr[i][j] = True
    while s:
        x, y = s.pop()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if arr[nx][ny]:
                continue
            cnt += 1
            s.append((nx,ny))
            arr[nx][ny] = True
    return cnt

def sol():
    m,n,k = map(int, input().split())
    # 빈공간이면 False 직사각형이 있으면 True
    arr = [[False]*n for _ in range(m)]
    # 직사각형에 해당하는 범위 체크
    for _ in range(k):
        x1,y1,x2,y2 = map(int,input().split())
        for i in range(y1,y2):
            for j in range(x1,x2):
                arr[i][j] = True
    
    # dfs를 통해 분리된 영역 넓이 구하기
    cnt = []
    for i in range(m):
        for j in range(n):
            if not arr[i][j]:
                cnt.append(dfs(i,j,m,n,arr))
    cnt.sort()
    print(len(cnt))
    print(*cnt)
    return 

sol()