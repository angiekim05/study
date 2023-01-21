import heapq
import sys
input = sys.stdin.readline

m,n = map(int,input().split())
miro = [list(map(int, list(input().strip()))) for _ in range(n)]

cnt = [[float("inf")]*m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
q = [(0,0,0)]
cnt[0][0] = 0
while q:
    d, x, y = heapq.heappop(q)

    if (x,y) == (n-1,m-1):
        print(d)
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        nd = d + miro[nx][ny]
        if cnt[nx][ny] <= nd:
            continue
        cnt[nx][ny] = nd
        heapq.heappush(q, (nd,nx,ny))