import sys
from heapq import heappop,heappush
input = sys.stdin.readline

m,n = map(int,input().split())
gido = []
c = []
for i in range(n):
    l=list(input().lower())
    for j in range(m):
        if l[j] == "c":
            c.append((i,j))
    gido.append(l)
d = [(0,1),(1,0),(0,-1),(-1,0)]

def sol(start,end):
    visited = [[[float("inf")]*4 for _ in range(m)] for _ in range(n)]
    i,j=start
    visited[i][j]=[1,1,1,1]
    q = []
    heappush(q,(1,i,j,0))
    heappush(q,(1,i,j,1))
    heappush(q,(1,i,j,2))
    heappush(q,(1,i,j,3))
    while q:
        t,x,y,dir = heappop(q)
        if (x,y) == end:
            continue
        for ii in range(4):
            nx,ny = x + d[ii][0] , y + d[ii][1]
            if nx >= n or 0 > nx or ny >= m or 0 > ny:
                continue
            if gido[nx][ny] == '*' or (dir+2)%4 == ii:
                continue
            if visited[nx][ny][ii] <= t: 
                continue
            if dir == ii:
                q.append((t,nx,ny,ii))
                visited[nx][ny][ii] = min(t,visited[nx][ny][ii])
            else:
                q.append((t+1,nx,ny,ii))
                visited[nx][ny][ii] = min(t+1,visited[nx][ny][ii])
    return visited[end[0]][end[1]]
ans = sol(*c)
print(min(ans)-1)