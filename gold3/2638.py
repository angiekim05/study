import sys
input = sys.stdin.readline
n,m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
cheese = n*m

# dfs
def check(i,j):
    cnt = 1
    visited = [[0]*m for _ in range(n)]
    q = [(i,j)]
    visited[i][j] = 1
    while q:
        x, y = q.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] or paper[nx][ny]:
                continue
            visited[nx][ny] = 1
            cnt += 1
            q.append((nx,ny))
    return visited, cnt

def sol():
    t = 0
    while True:
        outside, cnt = check(0,0)
        cnt = n*m - cnt
        if cnt > 0:
            t += 1
            for i in range(1,n-1):
                for j in range(1,m-1):
                    if paper[i][j] == 0:
                        continue
                    # 공기 접촉 여부
                    contact = outside[i-1][j] + outside[i+1][j] + outside[i][j-1] + outside[i][j+1]
                    if contact >= 2:
                        paper[i][j] = 0
                        cnt -= 1
                    if cnt == 0:
                        return t
        else:
            return t
print(sol())