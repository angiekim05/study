import sys
input = sys.stdin.readline

n,k = map(int,input().split())
sq = []
size = []
for i in range(n):
    p = list(map(int,input().split()))
    sq.append(p)
    size.append(abs(p[0]-p[2])*abs(p[1]-p[3]))
    
for i in range(n-1):
    x1,y1,x2,y2 = sq[i]
    w,h = abs(x2-x1),abs(y2-y1)
    temp = [[1]*(w) for _ in range(h)]
    for j in range(i+1,n):
        p = sq[j]
        if p[0] <= x1 <= p[2] and p[0] <= x2 <= p[2] and p[1] <= y1 <= p[3] and p[1] <= y2 <= p[3]:
            size[j] = 0
        elif p[0] <= x1 <= p[2] and p[1] <= y1 <= p[3]:
            for xx in range(abs(p[2]-x1)):
                for yy in range(abs(p[3]-y1)):
                    temp[h-yy-1][xx] = 0
        elif p[0] <= x1 <= p[2] and p[1] <= y2 <= p[3]:
            for xx in range(abs(p[2]-x1)):
                for yy in range(abs(y2-p[1])):
                    temp[yy][xx] = 0
        elif p[0] <= x2 <= p[2] and p[1] <= y1 <= p[3]:
            for xx in range(abs(x2-p[0])):
                for yy in range(abs(p[3]-y1)):
                    temp[h-yy-1][w-xx-1] = 0
        elif p[0] <= x2 <= p[2] and p[1] <= y2 <= p[3]:
            for xx in range(abs(x2-p[0])):
                for yy in range(abs(y2-p[1])):
                    temp[yy][w-xx-1] = 0
        elif x1 <= p[0] <= x2 and x1 <= p[2] <= x2 and y1 <= p[1] <= y2 and y1 <= p[3] <= y2:
            sx,sy = abs(y2-p[3]), abs(x1-p[0])
            for xx in range(abs(p[0]-p[2])):
                for yy in range(abs(p[1]-p[3])):
                    print("t",w,h,sx,sy,sx+yy,sy+xx)
                    temp[sx+yy][sy+xx] = 0

        if size[i] == 0:
            break
        size[i] = sum([sum(temp[z]) for z in range(h)])

ans = [(s,idx+1) for idx,s in enumerate(size)]
ans.sort()
for s, idx in ans[:k]:
    print(idx,end=" ")