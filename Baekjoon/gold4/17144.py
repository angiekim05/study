# R*C 크기의 array, 각 칸에 미세먼지의 양
# 공기청정기는 1열에 설치 & 크기는 2행(2*1)
# 1초동안 아래 두가지 반응이 순서대로 일어남
# 1. 미세먼지 확산
#   1.1. 상하좌우로 확산
#   1.2. 공기청정기나 벽 밖으로 확산 안됨
#   1.3. 확산되는 양은 미세먼지의 양//5
#   1.4. 확산되고 남는 양은 원래 있던 양에서 확산된 양만큼 뺀 것 
#         A[i][j] - (A[i][j]//5 * 확산된 칸 개수)
#   ** 확산은 동시다발적으로 일어남!!

# 2. 공기청정기 작동
#   2.1. 위쪽 공기청정기는 반시계방향으로 바람 순환 (사각형으로 순환 > ^ < v)
#        아래쪽 청정기는 시계방향으로 순환 (> v < ^)
#   2.2. 바람이 불면 미세면지는 바람 방향으로 한칸씩 이동
#   2.3. 순환을 통해 공기청정기로 들어간 미세먼지는 모두 정화
#  ** 공기청정기는 위에 두칸 아래 두칸 떨어져 있다!!

# T초 후 미세먼지의 총 양

import sys
from collections import deque

def diffusion(array,r,c): # loc1,loc2는 공기청정기 위치
    diffused = [deque([0]*c) for _ in range(r)] # 확산 후 array
    for x in range(r):
        for y in range(c):
            if array[x][y] > 0: # 미세먼지가 있으면
                diffused[x][y] += array[x][y]
                k = array[x][y]//5 # 확산되는 양
                # 사방에 확산 가능 영역 탐색 후 확산된 양 더해주기
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < r and 0 <= ny < c: # 공간이 있다면
                        if array[nx][ny] == -1: # 공기청정기 위치는 피하기
                            continue
                        diffused[nx][ny] += k # 미세먼지 확산
                        diffused[x][y] -= k # 확산된 만큼 빼주기
    return diffused

def airCleaner(array,r,c,cleaner):
    # 반시계방향 + 시계방향
    # 순차적으로 한칸씩 이동할 것
    dir = [(0,1),(-1,0),(0,-1),(1,0),(0,1),(1,0),(0,-1),(-1,0)]
    dir_idx = 0
    for start in cleaner:
        temp = 0
        x,y = start, 1
        while True:
            # 만약 공기청정기 위치로 왔다면 멈춤
            if x == start and y == 0:
                break
            # 이전에 담아 놓은 미세먼지를 지금 위치에 놓고
            # 지금 미세먼지는 다음으로 옮기도록 임시로 담아놓음
            array[x][y], temp = temp, array[x][y]
            # 다음 위치로 이동
            nx,ny = x + dir[dir_idx][0], y + dir[dir_idx][1]
            # 만약 범위가 넘어가면 방향을 바꿈
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                dir_idx += 1
                x,y = x + dir[dir_idx][0], y + dir[dir_idx][1]
            else:
                x,y = nx,ny
        dir_idx += 1 # 다음 사이클로 이동 (시계방향)
        # 공기청정기 들어가면 미세먼지 0
        array[start][0] = 0
    return array

input = sys.stdin.readline
r,c,t = map(int,input().split())
array = []
cleaner = []
for i in range(r):
    temp = deque(map(int,input().split()))
    if temp[0] == -1:
        cleaner.append(i)
    array.append(temp)

for _ in range(t):
    array = diffusion(array,r,c)
    array = airCleaner(array,r,c,cleaner)

answer = 0
for i in range(r):
    answer += sum(array[i])

print(answer)