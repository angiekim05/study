def go(x,y):
    return 0<=x<n and 0<=y<n

def find(q,key):
    visited = [[0] * n for _ in range(n)]
    visited[q[0][0]][q[0][1]] = 1
    temp = []
    while q:
        x,y = q.pop()
        temp.append((x, y))
        arr[x][y] = -1 # 경로를 -1로 초기화
        for dx,dy in dir:
            nx, ny = x+dx,y+dy
            if not go(nx,ny) or visited[nx][ny] or not arr[nx][ny]:
                continue
            if arr[nx][ny] == key:
                visited[nx][ny] = 1
                q.append((nx,ny))
                break
    return temp
def find_team(x,y):
    memb = find([(x,y)],2)
    head, tail = 0, len(memb)
    for dx,dy in dir:
        nx, ny = memb[-1][0] + dx, memb[-1][1] + dy
        if go(nx, ny) and arr[nx][ny] == 3:
            temp = find([(nx,ny)],4)
            memb += temp
    return [head,tail,1,memb]

def move(num):
    head,tail,d,memb = team[num]
    # 한 칸 전진
    head = (head-d)%len(memb)
    tail = (tail-d)%len(memb)
    team[num][0] = head
    team[num][1] = tail
    # 번호 다시 부여
    cur = head
    idx = 1
    while True:
        x,y = memb[cur]
        arr[x][y] = (num,idx)
        if cur == tail:
            break
        cur = (cur+d)%len(memb)
        idx += 1
    tail_next = (cur + d) % len(memb) #
    if tail_next != head: # 꼬리 바로 다음이 머리가 아니면 한 칸 이동했음으로 마지막이 다시 -1
        x,y = memb[tail_next]
        arr[x][y] = -1

def throw(idx,ball_way):
    if ball_way == 0:
        for i in range(n):
            if arr[idx][i] == 0 or arr[idx][i] == -1:
                continue
            # hit
            t_num,m_num = arr[idx][i]
            score[t_num] += m_num**2
            # head와 tail 바꾸기
            h,t,d,memb = team[t_num]
            team[t_num] = [t,h,d*(-1),memb]
            return
    elif ball_way == 1:
        for i in range(n):
            nx = n-1-i
            if arr[nx][idx] == 0 or arr[nx][idx] == -1:
                continue
            t_num,m_num = arr[nx][idx]
            score[t_num] += m_num**2
            # head와 tail 바꾸기
            h,t,d,memb = team[t_num]
            team[t_num] = [t,h,d*(-1),memb]
            return
    elif ball_way == 2:
        for i in range(n):
            if arr[n-1-idx][n-1-i] == 0 or arr[n-1-idx][n-1-i] == -1:
                continue
            t_num,m_num = arr[n-1-idx][n-1-i]
            score[t_num] += m_num**2
            # head와 tail 바꾸기
            h,t,d,memb = team[t_num]
            team[t_num] = [t,h,d*(-1),memb]
            return
    else:
        for i in range(n):
            if arr[i][n-1-idx] == 0 or arr[i][n-1-idx] == -1:
                continue
            t_num,m_num = arr[i][n-1-idx]
            score[t_num] += m_num**2
            # head와 tail 바꾸기
            h,t,d,memb = team[t_num]
            team[t_num] = [t,h,d*(-1),memb]
            return


n,m,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dir = ((0,1),(-1,0),(0,-1),(1,0))
team = []
score = [0]*m
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            team.append(find_team(i,j))

for round_ in range(k):
    # 한 칸 이동
    for i in range(m):
        move(i)

    # 공 던짐
    idx = round_%n
    ball_way = (round_//n)%4
    throw(idx,ball_way)
    # print(idx,ball_way)
    # print(team)
    # print(*arr,sep="\n")
    # print(score)
    # print()

print(sum(score))
