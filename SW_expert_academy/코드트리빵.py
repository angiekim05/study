n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
store = [list(map(int, input().split())) for _ in range(m)]

# 행이 작고 열이 작은 위치에 먼저 도달할 수 있는 상하좌우 순서
dx = (-1, 0, 0, 1)
dy = (0, -1, 1, 0)

# 시작 캠프 위치 찾기
def bfs(x, y):
    q = [(x - 1, y - 1)]
    visited = [[0] * n for _ in range(n)]
    visited[x - 1][y - 1] = 1
    while q:
        new_q = []
        for x, y in q:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] != 9:
                    visited[nx][ny] = 1
                    if arr[nx][ny] == 1:
                        arr[nx][ny] = 9
                        return nx, ny
                    new_q.append((nx, ny))
        q = new_q

suc = 0
t = 0
data = []
while True:
    # 모두 편의점 갔다면 멈춤
    if suc == m:
        break
    # m분에 m번 사람 베이스 캠프로 이동, 시작 위치와 이동 경로 visited 를 초기화해줌
    if t < m:
        cx, cy = bfs(*store[t])
        data.append([[(cx, cy)], [[0] * n for _ in range(n)]])
        data[t][1][cx][cy] = 1
        
    # 시간 마다 격자 안 모든 사람들 한칸 이동
    for i in range(min(t, m)):
        q = data[i][0] # 다음 이동 경로가 담긴 q
        v = data[i][1] # visited 정보가 담긴 v
        # q가 없다는 것은 이미 편의점으로 이동을 완료한 사람임 pass
        if not q:
            continue
        
        # 한칸 이동을 위한 bfs
        def bfs_(q, visited):
            global suc
            new_q = []
            # print(q)
            for x, y in q:
                for ii in range(4):
                    nx, ny = x + dx[ii], y + dy[ii]
                    if 0 <= nx < n and 0 <= ny < n:
                        if visited[nx][ny]:  # 방문한 곳 넘어가기
                            continue
                        if arr[nx][ny] == 9: # 막힌 곳 넘어가기
                            continue
                        visited[nx][ny] = 1 
                        # 편의점에 도달하면 장소 막고 성공횟수 + 1
                        if nx == store[i][0]-1 and ny == store[i][1]-1:
                            arr[nx][ny] = 9
                            suc+=1
                            return [],[]
                        new_q.append((nx, ny))
            return new_q, visited

        data[i][0], data[i][1] = bfs_(q, v)
    
    # 시간 추가
    t += 1
    
print(t)
