from collections import deque

# 맨허튼거리
def dist(r1,c1,r2,c2):
    return abs(r1-r2)+abs(c1-c2)

# i,j 위치 주변에 사람있는지 체크
def bfs(i,j,room):
    q = deque()
    q.append((i,j))
    visited = [[0]*5 for _ in range(5)]
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        if dist(i,j,x,y) > 2:
            continue
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x + dx, y + dy
            # 범위 벗어나면 pass
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            # 이미 방문했거나 벽이면 pass
            if visited[nx][ny] or room[nx][ny] == "X":
                continue
            # 맨해튼 거리 2 이내 사람있는지만 확인하면 됨으로 넘어가면 pass
            if dist(i,j,nx,ny) > 2:
                continue
            # 거리 2 이내 사람이 있다면 거리두기 안지켜짐!
            if room[nx][ny] == "P":
                return False
            # 방문 체크하고 이동
            visited[nx][ny] = 1
            q.append((nx,ny))
    
    # 사람이 없었다면 거리두기 지켜짐!
    return True

# 방 하나 검사
def room(room):
    #응시자 위치에서 bfs로 주변 사람있는지 체크
    for i in range(len(room)):
        for j in range(len(room[0])):
            if room[i][j] == "P":
                # 거리두기 실패면 0 바로 탈락
                if not bfs(i,j,room):
                    return 0
    return 1  

def solution(places):
    answer = []
    for place in places:
        answer.append(room(place))

    return answer

# print(solution(	[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))