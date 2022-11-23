# 모든 위치에서 최단거리이동(bfs)을 통해 도착할 수 있는 가장 먼 육지 탐색
# BFS
def bfs(i,j):
    q = deque()
    q.append((i,j,0))
    visited = [[0]*c for _ in range(r)]
    visited[i][j] = 1

    while q:
        x,y,d = q.popleft()
        
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny = x+dx, y+dy
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if visited[nx][ny] or treasure_map[nx][ny]=="W":
                continue
            q.append((nx,ny,d+1))
            visited[nx][ny] = 1

    return d

from collections import deque
import sys
input = sys.stdin.readline
r,c = map(int,input().split())
treasure_map = [input().strip() for _ in range(r)]
answer = 0

for i in range(r):
    for j in range(c):
        if treasure_map[i][j] == "L":
            answer = max(answer, bfs(i,j))

print(answer)