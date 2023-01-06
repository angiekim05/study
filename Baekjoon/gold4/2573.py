import sys
input = sys.stdin.readline

n, m = map(int, input().split())
island = [list(map(int,input().split())) for _ in range(n)]
dx = (0,0,-1,1)
dy = (-1,1,0,0)

# 분리된 땅을 count하는 함수 & 동시에 주변에 0이 있다면 빙산을 -1씩 녹임
def count():
    visited = [[0]*m for _ in range(n)]
    cnt = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if island[i][j] > 0 and not visited[i][j]:
                q = [(i,j)]
                visited[i][j] = 1
                while q:
                    x,y = q.pop()
                    for di in range(4):
                        nx,ny = x+dx[di], y+dy[di]
                        # 방문했다면 다시 갈 필요가 없으며, 이미 빙산이 남아있단 뜻으로 -1도 안해줌
                        if nx < 0 or ny < 0 or n <= nx or m <= ny or visited[nx][ny]:
                            continue
                        if island[nx][ny] > 0: # 다음 빙산이 남아있다면 방문처리하고 이동
                            visited[nx][ny] = 1
                            q.append((nx,ny))
                        else: # 다음 빙산이 없다면 주변이 바다임으로 현재 위치가 -1 녹음
                            island[x][y]-=1
                cnt += 1
    return cnt

y = -1 # count가 먼저 들어가기 때문에 변화 전에 count한 것은 안쳐주기 위해서 1을 뺌
while True:
    y += 1
    cnt = count()
    # print(*island, sep="\n") # 땅의 변화 확인
    if cnt >= 2: # 땅이 두개 이상으로 나눠졌을 경우 해당 연도를 print
        print(y)
        break
    elif cnt == 0: # 땅이 0개가 되도록 2개 이상으로 안나눠졌다면 0 print
        print(0)
        break