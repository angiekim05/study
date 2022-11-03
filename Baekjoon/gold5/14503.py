import sys
input = sys.stdin.readline
n,m = map(int,input().split())
r,c,d = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(n)]
direction = ((-1,0),(0,1),(1,0),(0,-1))
clean_area = 1
cleaned = [[0]*m for _ in range(n)]
current = [(r,c,d)]
cleaned[r][c] = 1

while current:
    x, y, d = current.pop()

    for i in range(1,5):
        nd = (d - i) % 4
        nx, ny = x + direction[nd][0], y + direction[nd][1]

        if nx < 1 or ny < 1 or nx >= n or ny >= m:
            continue
        if area[nx][ny] or cleaned[nx][ny]:
            continue
        current.append((nx,ny,nd))
        cleaned[nx][ny] = 1
        clean_area += 1
        break

    else:
        nx, ny = x + direction[d-2][0], y + direction[d-2][1]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if area[nx][ny]:
            continue
        current.append((nx,ny,d))
        cleaned[nx][ny] = 1

print(clean_area)