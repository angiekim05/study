# https://www.codetree.ai/training-field/frequent-problems/problems/firewall-installation?&utm_source=clipboard&utm_medium=text

# 방화벽 3개 추가했을 때 불이 안 퍼지는 영역이 최대가 되어야 함.
from collections import deque

# 영역 크기
n,m = map(int, input().split())

# info 0: 공백, 1: 방화벽, 2: 불
arr = []
fire = []
non_fire = n*m - 3 # 벽 3개 추가할 예정
dxdy = [(0,1),(0,-1),(1,0),(-1,0)]

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        if arr[i][j] == 1:
            non_fire -= 1
        elif arr[i][j] == 2:
            fire.append((i,j))
            non_fire -= 1

# 불이 퍼지는 함수
def bfs(non_fire):
    fire_ = deque(fire)
    visited = [[0]*m for _ in range(n)]
    while fire_:
        x,y = fire_.pop()
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if arr[nx][ny]:
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = 1 # 불이 번짐
            non_fire -= 1
            fire_.append((nx,ny))
    return non_fire

# 벽 3개 세우기 (중복 탐색 수정 필요)
def make_wall(cnt):
    global ans
    if cnt == 3:        
        ans = max(ans,bfs(non_fire))
        return
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                make_wall(cnt+1)
                arr[i][j] = 0

ans = 0
make_wall(0)
print(ans)
