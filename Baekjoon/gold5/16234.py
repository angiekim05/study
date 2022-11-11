# 문제
# 인구 이동은 하루 동안 더이상 인구 이동이 없을 때까지 지속된다!
# 인구 이동은 L <= abs(A[r][c]-A[nr][nc]) <= R 인 모든 인접 연합 국가에서 일어나고
# 각 연합 국가들은 총 인구수 // 국가수 의 인구로 재배치됨
# output은 총 며칠 동안 인구 이동이 일어나는지!

import sys
from collections import deque
input = sys.stdin.readline
def sol():
    n,L,R = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]

    # 최대 인구이동 일수
    lastday = 2000
    for day in range(lastday):
        visited = [[0]*n for _ in range(n)] # 날마다 visited 새로 만들어줌
        moved = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j]: # 장소를 방문했다면 이미 인접 국가를 확인했기 때문에 지나가도 됨
                    continue
                # bfs
                q = deque()
                # 지금 있는 장소 update
                q.append((i,j))
                visited[i][j] = 1
                population = A[i][j]
                Union = [] # 연합 국가들
                while q:
                    x, y = q.popleft()
                    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nx, ny = x+dx, y+dy # 연합 국가 위치
                        if 0 > nx or nx >= n or 0 > ny or ny >= n: # 범위 밖 pass
                            continue
                        if visited[nx][ny]: # 이미 들린 곳은 넘어가기
                            continue
                        diff = abs(A[x][y]-A[nx][ny])
                        if diff < L or R < diff: # 인구차이가 기준보다 적거나 많으면 pass (연합 국가 조건)
                            continue
                        population += A[nx][ny]
                        q.append((nx,ny))
                        Union.append((nx,ny))
                        visited[nx][ny] = 1

                if Union: # 연합국가가 있다면 새로운 인구수로 바꿔줌
                    moved = 1 # 이동을 했음을 체크
                    Union += [(i,j)] # 시작한 국가 포함 인구 이동
                    new_pop = population // (len(Union)) # 새로운 인구수 = 총 인구수 // 국가수
                    for x,y in Union:
                        A[x][y] = new_pop
                    

        if not moved: # 더이상 이동이 없었다면 멈춤
            return day

    else:
        return 2000 # 마지막날까지 이동했다면
print(sol())

# -------------------------------------------------------------

## 다른 코드 참고!
### Point 1. (i,j)를 탐색했다면 적어도 (i,j)를 기준으로 상하좌우를 조사하기 때문에
### 초기에 격자 모양으로 탐색을 시작하면 절반은 안 둘러봐도 괜찬음!
### Point 2. 연합 국가 사이에 인구 이동이 있다면 해당 국가들의 주변을 다시 탐색
### 인구수에 변동이 있기 때문에 해당 국가들의 주변 국가들과 연합 가능 여부를 다시 확인해야 하기 때문
### 새로운 인구 이동이 필요한지 확인하고 더이상 필요하지 않다면
### 주변 국가들이 연합국가 조건을 만족하지 않은 것이기 때문에 종료하면 됨.
### => 불필요한 반복(매일 모든 i,j 방문)을 안하기 때문에 시간이 훨씬 단축됨!!

### Point 3. visited 를 하나로 사용하며 day로 업데이트를 해줌으로써
### 매번 visited를 새로 생성해주지 않아도 됨!!

import sys
from collections import deque
input = sys.stdin.readline
def sol():
    n,L,R = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]

    # 격자 모양으로 탐색 시작
    search_area = deque([(i,j) for i in range(n) for j in range(i%2,n,2)])
    day = -1
    visited = [[-1]*n for _ in range(n)] # 날짜별 visited

    while search_area: # 아직 탐색할 국가가 남아 있다면 (연합국으로 인구 이동이 있었다면) 다음날로 이동
        day += 1 
        q = deque()
        for _ in range(len(search_area)):
            i,j = search_area.popleft()

            if visited[i][j] == day: # 같은 날짜에 장소를 방문했다면 이미 연합 국가를 확인했기 때문에 지나가도 됨
                continue
                
            # bfs
            q.append((i,j)) # 지금 있는 장소
            visited[i][j] = day
            population = A[i][j] # 총 인구수
            Union = [(i,j)] # 연합 국가들
            while q:
                x, y = q.popleft()
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx, ny = x+dx, y+dy # 다음 연합 국가 위치
                    if 0 > nx or nx >= n or 0 > ny or ny >= n: # 범위 밖 pass
                        continue
                    if visited[nx][ny] == day: # 같은 날짜에 이미 들린 곳은 넘어가기
                        continue
                    diff = abs(A[x][y]-A[nx][ny]) # 인구차
                    if diff < L or R < diff: # 인구차가 기준보다 적거나 많으면 pass (연합 국가 조건 불만족)
                        continue
                    population += A[nx][ny]
                    q.append((nx,ny))
                    Union.append((nx,ny))
                    visited[nx][ny] = day

            if len(Union) > 1: # 연합 국가가 있다면 새로운 인구수로 바꿔줌
                new_pop = population // (len(Union)) # 새로운 인구수 = 총 인구수 // 국가수
                for x,y in Union:
                    A[x][y] = new_pop
                    search_area.append((x,y))
    return day
print(sol())