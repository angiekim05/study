# (n-1,m-1) 위치에서 (0,0) 까지의 경우의 수를 역으로 채우는 방법 사용

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,y):
    if x == n-1 and y == m-1:
        return 1
    
    # 방문한 적이 있다면, 해당 위치에서 출발하는 경우의 수 return
    if visited[x][y] != -1:
        return visited[x][y]

    cnt = 0 # (x,y)에서 (n-1,m-1)까지 방법 경우의 수
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m: # 지도 밖이면 pass
            continue
        if maps[nx][ny] >= maps[x][y]: # 내리막길이 아니면 pass
            continue
        cnt += dfs(nx,ny)

    visited[x][y] = cnt
    return cnt


n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
dx,dy = (0,0,1,-1),(1,-1,0,0)
visited = [[-1]*m for _ in range(n)]
print(dfs(0,0))