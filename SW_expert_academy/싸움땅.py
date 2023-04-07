def move(x,y,d):
    nx,ny = x+dir[d][0], y+dir[d][1]
    if 0<=nx<n and 0<=ny<n:
        return nx,ny,d
    return x+dir[(d+2)%4][0], y+dir[(d+2)%4][1], (d+2)%4

def loser_move(x,y,d):
    nx, ny = x + dir[d][0], y + dir[d][1]
    if 0 <= nx < n and 0 <= ny < n and not player[nx][ny]:
        return nx, ny, d
    return loser_move(x,y,(d+1)%4)
def fight(a,b):
    x,y = p[a][-1]+p[a][-2],p[b][-1]+p[b][-2]
    point = abs(x-y)
    if x == y:
        if p[a][-2] > p[b][-2]: # 초기 능력 비교
            return a,b,point
    elif x > y:
        return a,b,point
    return b,a,point

def put_down(x,y,num):
    if p[num][-1]: # 플레이어가 총을 가지고 있다면 총 내려놓기
        gun[x][y].append(p[num][-1])
        gun[x][y].sort()
        p[num][-1] = 0

def get_gun(x,y,num):
    if not gun[x][y]: # 자리에 총이 없으면 종료
        return
    put_down(x,y,num)
    # 공격력 제일 큰 총 가지기
    new_gun = gun[x][y].pop()
    p[num][-1] = new_gun



def solution():
    for _ in range(k):
        for i in range(1,m+1):
            x,y,d,s,g = p[i]
            nx,ny,nd = move(x,y,d)
            print(i,x,y,nx,ny)
            p[i][2] = nd
            if not player[nx][ny]:
                get_gun(nx,ny,i)
                p[i][0], p[i][1] = nx, ny
                player[x][y] = 0
                player[nx][ny] = i
            else:
                win,lose,point = fight(i,player[nx][ny])
                print(win,lose,point)
                if i == win: # 새로 온 사람이 승리
                    # 이긴 사람 포인트 획득
                    score[win-1] += point
                    # 새로온 이긴 사람 자리 차지하기
                    p[win][0], p[win][1] = nx,ny
                    player[x][y] = 0
                    player[nx][ny] = win
                    # 진 사람 총 내려 놓기
                    put_down(nx,ny,lose)
                    # 진 사람 이동해서 빈자리의 총 얻기
                    lose_x,lose_y,lose_d = loser_move(nx,ny,p[lose][2])
                    p[lose][0],p[lose][1],p[lose][2] = lose_x,lose_y,lose_d
                    player[lose_x][lose_y] = lose
                    get_gun(lose_x,lose_y,lose)
                    # 이긴 사람 총 얻기
                    get_gun(nx,ny,win)
                else: # 기존에 있던 사람 승리
                    # 이긴 사람 포인트 획득
                    score[win-1] += point
                    # 진 사람 총 내려 놓기
                    put_down(nx,ny,lose)
                    # 새로 왔지만 진 사람 이동해서 빈자리의 총 얻기
                    player[x][y] = 0
                    lose_x,lose_y,lose_d = loser_move(nx,ny,p[lose][2])
                    p[lose][0],p[lose][1],p[lose][2] = lose_x,lose_y,lose_d
                    player[lose_x][lose_y] = lose
                    get_gun(lose_x,lose_y,lose)
                    # 이긴 사람 총 얻기
                    get_gun(nx,ny,win)
            print(*player, sep="\n")
            print()
            print(*gun, sep="\n")
            print()
        print(*p,sep="\n")
        print()
n,m,k = map(int,input().split())
gun = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 0:
            gun[i].append([])
        else:
            gun[i].append([temp[j]])
player = [[0]*n for _ in range(n)]
p = [[]]
for i in range(1,m+1):
    x,y,d,s = map(int, input().split())
    p.append([x-1,y-1,d,s,0])
    player[x-1][y-1] = i
print(*p,sep="\n")
dir = ((-1,0),(0,1),(1,0),(0,-1))
score = [0]*m
solution()
print(score)
