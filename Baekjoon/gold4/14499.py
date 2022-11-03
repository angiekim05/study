# 주사위 바닥 = 1 상단 = 6
#   2
# 4 1 3
#   5
#   6
# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4

n,m,x,y,k = map(int, input().split())
jido = [list(map(int,input().split())) for _ in range(n)]
order = list(map(int,input().split()))
dx = (0,0,0,-1,1)
dy = (0,1,-1,0,0)

dice = [0]*6
for d in order:
    nx, ny = x + dx[d], y + dy[d]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
    x, y = nx, ny
    if d == 1: # 오른쪽으로 1칸 굴림
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif d == 2: # 왼쪽 한칸 => 오른쪽의 반대
        dice[2], dice[5], dice[0], dice[3] = dice[0], dice[2], dice[3], dice[5]
    elif d == 3: # 위로 
        dice[4], dice[0], dice[5], dice[1] = dice[0], dice[1], dice[4], dice[5]
    elif d == 4: # 아래로
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    
    if jido[x][y] == 0:
        jido[x][y] = dice[0]
    else:
        jido[x][y],dice[0] = 0,jido[x][y]

    print(dice[-1])