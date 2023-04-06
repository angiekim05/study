from heapq import heappop,heappush
dx = [1,0,-1,0]
dy = [0,1,0,-1]
num = 0
while True:
    num += 1
    n = int(input())
    if n == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[float("inf")]*n for _ in range(n)]
    dist[0][0] = arr[0][0]
    q = [(dist[0][0],0,0)]
    while q:
        d,x,y = heappop(q)
        if x == y == n-1:
            break
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                nd = d + arr[nx][ny]
                if dist[nx][ny] > nd:
                    dist[nx][ny] = nd
                    heappush(q,(nd,nx,ny))
    print(f"Problem {num}: {dist[-1][-1]}")
