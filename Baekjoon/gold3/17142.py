from collections import deque
import sys
input = sys.stdin.readline

def bfs(lab, virus):
    visited = [[0]*n for _ in range(n)]
    for i,j,_ in virus:
        visited[i][j] = -1
    for i,j in wall:
        visited[i][j] = -2
    cnt = 0
    while virus:
        x,y,c = virus.popleft()
        if lab[x][y] != 2:
            cnt = max(cnt,c)
        for dx,dy in dir:
            nx,ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if lab[nx][ny] == 1:
                continue               
            else:
                visited[nx][ny] = c+1
                virus.append((nx,ny,c+1))
    # print(*visited, sep="\n")
    # print(c)
    for i in range(n):
        if 0 in visited[i]:
             return 5000
    return cnt

def comb(lst,n):
	ret = []
	if n > len(lst): return ret
	if n == 1:
		for i in lst:
			ret.append([i])
	elif n>1:
		for i in range(len(lst)-n+1):
			for temp in comb(lst[i+1:],n-1):
				ret.append([lst[i]]+temp)
	return ret

# 연구소크기, 바이러스수
n,m = map(int, input().split())
dir = [(0,1),(1,0),(0,-1),(-1,0)]
lab = []
virus = []
wall = []
for i in range(n):
    lab.append(list(map(int, input().split())))
    for j in range(n):
        if lab[i][j] == 1:
            wall.append((i,j))
        if lab[i][j] == 2:
            virus.append((i,j,0))

if len(wall)+len(virus) == n**2:
    print(0)
else:
    ans = 5000
    # virusCm 조합을 구해서 모든 경우 중 최소값을 찾음
    for v in comb(virus, m):
        ans = min(ans,bfs(lab,deque(v)))
    print(ans if ans < 5000 else -1)