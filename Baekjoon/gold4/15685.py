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
    while g > 0:
        g -= 1
        for i in range(len(nodes)-1,-1,-1):
            d = nodes[i]
            nd = (d+1)%4
            ex,ey = ex+dir[nd][0],ey+dir[nd][1]
            nodes.append(nd)
            add_vertex(ex,ey)
    return

dir = [(1,0),(0,-1),(-1,0),(0,1)]
s_dir = [(-0.5,-0.5),(-0.5,0.5),(0.5,-0.5),(0.5,0.5)]
sq = dict()

n = int(input())
p = [curve(*list(map(int,input().split()))) for _ in range(n)]

print(count(sq))