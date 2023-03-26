import sys
input = sys.stdin.readline

def add_vertex(x,y):
    for k in range(4):
        vx,vy = x+s_dir[k][0],y+s_dir[k][1]
        if (vx,vy) in sq:
            sq[(vx,vy)][k] = 1
        else:
            temp = [0]*4
            temp[k] = 1
            sq[(vx,vy)] = temp

def count(sq):
    cnt = 0
    for k in sq.keys():
        if sum(sq[k]) == 4:
            cnt += 1
    return cnt

def curve(x,y,d,g):
    ex,ey = x+dir[d][0], y+dir[d][1]
    add_vertex(x,y)
    add_vertex(ex,ey)
    nodes = [d]
    for _ in range(g):
        for i in range(len(nodes)-1,-1,-1):
            d = nodes[i]
            nd = (d+1)%4
            nodes.append(nd)
            ex,ey = ex+dir[nd][0],ey+dir[nd][1]
            add_vertex(ex,ey)
    return

dir = [(1,0),(0,-1),(-1,0),(0,1)]
s_dir = [(-0.5,-0.5),(-0.5,0.5),(0.5,-0.5),(0.5,0.5)]
sq = dict()

n = int(input())
p = [curve(*list(map(int,input().split()))) for _ in range(n)]

print(count(sq))

# ------------------------------------------------------------------
# 100 * 100 배열 내에서만 드래곤 커브가 생긴다
# 따라서 그 조건 안에서만 찾으면 됨

import sys
input = sys.stdin.readline

def curve(x,y,d,g):
    # 꼭지점끝
    ex,ey = x+dir[d][0], y+dir[d][1]
    # 시작점과 시작하는 선분의 끝점 위치 저장
    arr[x][y] = 1
    arr[ex][ey] = 1
    nodes = [d]
    for _ in range(g):
        for i in range(len(nodes)-1,-1,-1):
            # 방향
            d = nodes[i]
            nd = (d+1)%4
            nodes.append(nd)

            # 다음 드래곤 커브를 이을 꼭지점 체크
            ex,ey = ex+dir[nd][0],ey+dir[nd][1]
            # 꼭지점의 위치 저장
            arr[ex][ey] = 1
    return

n = int(input())
arr = [[0]*101 for _ in range(101)] # 점의 위치 저장
dir = [(1,0),(0,-1),(-1,0),(0,1)]
for _ in range(n):
    curve(*list(map(int,input().split())))

# 네 점이 모두 있으면 카운트
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]: 
            ans += 1
print(ans)