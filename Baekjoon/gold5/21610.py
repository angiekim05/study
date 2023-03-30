import sys
input = sys.stdin.readline

n,m = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
c = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
dir = [0,(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
dir_ = [(-1,-1),(-1,1),(1,1),(1,-1)]

for _ in range(m):
    d,s = map(int, input().split())
    dx,dy = dir[d][0]*s,dir[d][1]*s
    
    cloud = [[0]*n for _ in range(n)]
    for i in range(len(c)):
        x,y = c[i]
        # move
        c[i] = (x+dx)%n, (y+dy)%n
        # rain
        box[(x+dx)%n][(y+dy)%n] += 1
        cloud[(x+dx)%n][(y+dy)%n] = 1
    
    for x,y in c:
        for dx_,dy_ in dir_:
            nx,ny = x+dx_, y+dy_
            if 0<=nx<n and 0<=ny<n and box[nx][ny]:
                # bug
                box[x][y] += 1

    new = []
    for x in range(n):
        for y in range(n):
            if not cloud[x][y] and box[x][y] >= 2:
                box[x][y] -= 2
                new.append((x,y))

    c = new
print(sum(map(sum,box)))