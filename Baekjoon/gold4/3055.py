import heapq
import sys
input = sys.stdin.readline

r,c = map(int, input().split())
arr = []
water = []
for i in range(r):
    temp = list(input().strip())
    arr.append(temp)
    for j in range(c):
        if temp[j] == "D":
            d = (i,j)
        elif temp[j] == "S":
            s = (i,j)
        elif temp[j] == "*":
            water.append((i,j))

dx = (0,0,1,-1)
dy = (1,-1,0,0)

def spread(water):
    new = []
    for x,y in water:
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<r and 0<=ny<c and arr[nx][ny] == ".":
                new.append((nx,ny))
                arr[nx][ny] = "*"
    return new

def bfs(s,d,water):
    x,y = s
    q = [(0,x,y)]
    visited = [[0]*c for _ in range(r)]
    visited[x][y] = 1
    bf_t = 0
    while q:
        t,x,y = heapq.heappop(q)

        if x == d[0] and y == d[1]:
            return t
        
        if bf_t < t:
            water = spread(water)
            bf_t = t

        if arr[x][y] == "*":
            continue

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                if arr[nx][ny] == "X":
                    continue
                if arr[nx][ny] == "*":
                    continue
                visited[nx][ny] = 1
                heapq.heappush(q,(t+1,nx,ny))
    return 0

ans = bfs(s,d,water)
print(ans if ans > 0 else "KAKTUS")