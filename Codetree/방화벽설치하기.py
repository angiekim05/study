# https://www.codetree.ai/training-field/frequent-problems/problems/firewall-installation?&utm_source=clipboard&utm_medium=text

# 방화벽 3개 추가했을 때 불이 안 퍼지는 영역이 최대가 되어야 함.
from collections import deque

# 영역 크기
n,m = map(int, input().split())

# info 0: 공백, 1: 방화벽, 2: 불
arr = [] # 공간 정보
fire = [] # 불이 있는 위치
empty = [] # 공백 즉 벽이 세워질 수 있는 위치
dxdy = [(0,1),(0,-1),(1,0),(-1,0)]

for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(m):
        if arr[i][j] == 0:
            empty.append((i,j)) # 공백 위치 추가
        elif arr[i][j] == 2:
            fire.append((i,j)) # 불 위치 추가

# 불이 퍼지는 함수
def bfs():
    non_fire = len(empty) - 3 # 세워질 벽 개수 제외한 공백 수
    fireq = deque(fire) # bfs를 위해 deque 사용
    visited = [[0]*m for _ in range(n)]
    while fireq:
        x,y = fireq.popleft()
        for dx, dy in dxdy:
            nx, ny = x + dx, y + dy
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if arr[nx][ny]: # 불이나 벽이 있는 위치 제외하고 빈공간 탐색
                continue
            if visited[nx][ny]: # 방문했던 곳 제외 (이미 불이 번진 곳)
                continue
            visited[nx][ny] = 1 # 불이 번짐
            non_fire -= 1 # 불이 번져 공백이 줄어듦
            fireq.append((nx,ny))
    return non_fire

def make_wall(cnt,idx):
    global ans
    if cnt == 3: # 벽이 세개 세워지면 공백의 수 세어보기
        ans = max(ans,bfs())
        return
    
    for i in range(idx,len(empty)): # 조합으로 찾는 것이기 때문에 이전에 벽 세운 곳 제외하기 위해 이전 idx 이후로 탐색 (1100 1010 1001 0110 0101 0011)
        arr[empty[i][0]][empty[i][1]] = 1 # 벽 세우기
        make_wall(cnt+1,i+1) # 다음 벽 세우러 가기
        arr[empty[i][0]][empty[i][1]] = 0 # 벽 다시 치우기

ans = 0
make_wall(0,0)
print(ans)
