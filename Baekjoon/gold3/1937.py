# 대나무가 많은 쪽으로 이동하는 팬터가 가장 많이 이동한 횟수를 구하는 문제

# DFS를 사용해 이동가능한 경로(이전보다 더 대나무가 많은 경로)로 이동하면서 이동횟수를 DP로 담음
# 재귀를 통해 DFS를 진행하면, 현재 위치의 DP에는 현재 위치에서 가장 멀리 갈 수 있는 이동 횟수를 담게 됨
# 주변에 자신보다 큰 숫자가 없으면 더이상 이동을 할 수 없기 때문에
# move[x][y] = 1 로만 바뀌고 이동 안 함
# return을 통해 돌아오면서 최종 도착지부터 1씩 증가하며 move에 이동횟수가 담김
# 다음 칸이 이미 채워진 칸이라면 해당 칸에서 최대 이동 횟수가 담긴 것이기 때문에 바로 return 받아 +1로 계산하면 됨
# 한번 dfs를 통과하면서 갈 수 있는 최대 길이를 계속 업데이트하면 대나무 숲에서 최대 이동 횟수를 구할 수 있음

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x,y):
    if move[x][y]:
        return move[x][y]
    move[x][y] = 1
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if nx < 0 or ny < 0 or nx >=n or ny >= n:
            continue
        if bamboo[nx][ny] > bamboo[x][y]:
            move[x][y] = max(move[x][y],dfs(nx,ny)+1)
    return move[x][y]

n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]
dx = (-1,0,1,0)
dy = (0,1,0,-1)
move = [[0]*n for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans,dfs(i,j))
print(ans)
print(*move,sep="\n")