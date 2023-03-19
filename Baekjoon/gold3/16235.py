import sys
from collections import defaultdict
input = sys.stdin.readline

n,m,k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# spot[i][j]는 현재 나무 정보, 내년 추가 나무 정보 (번식), 양분 정보가 담김
spot = [[[[],5] for j in range(n)] for i in range(n)]
for _ in range(m):
    x,y,z = map(int, input().split())
    spot[x-1][y-1][0].append(z)

for i in range(n):
    for j in range(n):
        if spot[i][j][0]:
            spot[i][j][0].sort()

for y in range(k):
    # print(*spot, sep="\n")
    # print()
    temp = defaultdict(int)
    for i in range(n):
        for j in range(n):
            for x in range(len(spot[i][j][0])):
                age = spot[i][j][0][x]
                # 봄
                if spot[i][j][1] >= age:
                    spot[i][j][1] -= age
                    spot[i][j][0][x] += 1
                    if spot[i][j][0][x] % 5 == 0:
                        temp[(i,j)] += 1
                # 여름
                else:
                    for t in range(x,len(spot[i][j][0])):
                        spot[i][j][1] += spot[i][j][0][t]//2
                    spot[i][j][0] = spot[i][j][0][:x]
                    break
            # 겨울
            spot[i][j][1] += a[i][j]
    # 가을
    for x,y in temp.keys():
        for r,c in d:
            nx,ny = x+r, y+c
            if 0<=nx<n and 0<=ny<n:
                spot[nx][ny][0] = [1]*temp[(x,y)] + spot[nx][ny][0]
ans = 0
for i in range(n):
    for j in range(n):
        ans += len(spot[i][j][0])
print(ans)