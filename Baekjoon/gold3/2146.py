# 섬을 구별하고 서로 다른 섬 사이 최단 거리를 구하는 문제
# 먼저 섬 구역별 표시를 하고, 시작점과 다른 번호의 섬에 도착한 거리를 서로 비교한다

from collections import deque
import sys
input = sys.stdin.readline

# dfs를 사용하여 numb로 섬의 번호를 표시하였다. (bfs를 사용해도 무관)
def find_island(i,j,numb):
    s = [(i,j)]
    while s:
        x,y = s.pop()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or n <= nx or n <= ny: # 지도 밖을 벗어나면 넘어가고
                continue
            if island[nx][ny]: # 이미 방문했을 경우에도 넘어간다.
                continue
            if arr[nx][ny] == 1:
                # 방문 체크와 함께 섬일 경우 바로 1이상의 numb를 표시한다.
                island[nx][ny] = numb
                s.append((nx,ny))

# 가장 단거리의 다른 섬을 찾기 위해서는 bfs를 사용하였다.
# 매번 새롭게 방문체크를 하면서 현재 위치에서 
# 가장 빠르게 도달하는 다른 섬까지의 거리를 return하고,
# 만약 다른 섬이 없다면 큰 수를 return 한다.
def bfs(i,j,numb):
    q = deque([(i,j,0)])
    visited = [[0]*n for _ in range(n)]
    while q:
        x,y,d = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or n <= nx or n <= ny:
                continue
            if visited[nx][ny]:
                continue
            if island[nx][ny] == 0: # 바다면 이동
                visited[nx][ny] = 1
                q.append((nx,ny,d+1))
            elif island[nx][ny] != numb: # 다른 섬 발견하면 거리를 반납
                return d
    return float("inf")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = (0,0,-1,1)
dy = (-1,1,0,0)

island = [[0]*n for _ in range(n)]
numb = 1
for i in range(n):
    for j in range(n):
        # island에 섬표시가 아직 안되었고, 주어진 arr에서 섬이라면 해당 섬을 탐색한다.
        if not island[i][j] and arr[i][j] == 1: 
            island[i][j] = numb
            find_island(i,j,numb)
            numb += 1

min_len = float("inf")
for i in range(n):
    for j in range(n):
        # 섬표시가 되어있다면 다른 섬까지의 최단거리 탐색
        if island[i][j] > 0: 
            min_len = min(min_len,bfs(i,j,island[i][j]))
print(min_len)