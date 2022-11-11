# 함수화 한 풀이가 1초정도 더 빨랐음 (3828ms -> 2556ms)
# 추측
# 1. while 문에서 break 보다 retrun 이 더 효율적인 것 같음
# 2. test case가 한번에 여러개 주어질 때 함수가 더 효율적? 

from collections import deque
import sys
input = sys.stdin.readline
night_step = ((-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))

t = int(input())
for _ in range(t):
    n = int(input())
    si,sj = tuple(map(int,input().split()))
    ei,ej = tuple(map(int,input().split()))

    # bfs
    def bfs(si,sj,ei,ej):
        q = deque()
        q.append((si,sj))
        visited = [[0]*n for _ in range(n)] # 이동 횟수를 담음
        visited[si][sj] = 1
        while q:
            x, y = q.popleft()

            if x == ei and y == ej:
                print(visited[x][y]-1) # 자기 자신 방문 횟수도 포함됨으로 이동횟수는 -1 해줘야함
                return
            
            for i in range(8):
                nx, ny = x + night_step[i][0], y + night_step[i][1] # 나이트의 이동 위치
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if visited[nx][ny]: # 이미 최소 이동 횟수가 담겨있으면 pass
                    continue
                visited[nx][ny] = 1 + visited[x][y] # 방문횟수는 이전 방문횟수 + 1
                q.append((nx,ny))
    bfs(si,sj,ei,ej)