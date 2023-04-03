# 빈칸을 셀때, 빈칸이 전혀 없는 경우도 고려해줘야함..

import sys
input = sys.stdin.readline

n = int(input())
room = [[0]*n for _ in range(n)]
like = dict()
pos = dict()
dx = (0,0,1,-1)
dy = (1,-1,0,0)

# 첫번째
x,a,b,c,d = map(int,input().split())
like[x] = [a,b,c,d]
room[1][1] = x
pos[x] = (1,1)

# 빈칸세기기
def blank(x,y):
    cnt = 0
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and room[nx][ny] == 0:
            cnt += 1
    return cnt

# 후보군 찾기 (친구수)
def check(x,y):
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and room[nx][ny] == 0:
            if (nx,ny) in candi.keys():
                candi[(nx,ny)] += 1
            else:
                candi[(nx,ny)] = 1

for idx in range(1, n**2):
    x,a,b,c,d = map(int,input().split())
    # 좋아하는 친구 담기
    like[x] = [a,b,c,d]
    
    #후보군 구하기
    candi = dict()
    for l in [a,b,c,d]:
        # 이미 자리 잡은 친구가 있다면 그 주위 자리 체크
        if l in pos.keys(): 
            check(*pos[l])
            
    # 후보군 있으면 조건 따져보기
    if candi:
        # 친구수 기준으로 정렬
        maxs = sorted(candi.items(), key= lambda k: [-k[1]])
        max_ = maxs[0][1]

        # 친구수가 동일한 후보군이 있는지 확인
        for i in range(1,1+len(maxs)):
            if maxs[i-1][1] < max_:
                i -= 1
                break
        
        # 친구수가 동일한 후보군이 없으면 그 자리에 번호 적고 pos에도 위치 입력
        if i == 1:
            room[maxs[0][0][0]][maxs[0][0][1]] = x
            pos[x] = maxs[0][0]

        # 후보군이 여럿이라면 후보군 주위의 빈칸수를 세줌
        else:
            candi = dict()
            for j in range(i):
                candi[maxs[j][0]] = blank(*maxs[j][0])
            
            # 빈칸수로 정렬해서 자리 잡기
            maxs = sorted(candi.items(), key= lambda k: [-k[1],k[0],k[1]])
            room[maxs[0][0][0]][maxs[0][0][1]] = x
            pos[x] = maxs[0][0]
            
    # 후보군 없으면 빈칸이 제일 많은 곳 찾기
    else:
        def find():
            max_ = 0
            max_pos = False
            for i in range(n):
                for j in range(n):
                    if room[i][j] == 0:
                        cnt = blank(i,j)
                        if cnt == 4:
                            return (i,j)
                        elif cnt > max_:
                            max_ = cnt
                            max_pos = (i,j)
                        elif not max_pos: #아직 위치정보가 없다면 (cnt가 0일 때)
                            max_pos = (i,j)
            return max_pos
        i,j = find()
        room[i][j] = x
        pos[x] = (i,j)

def score():
    ans = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(4):
                nx,ny = i+dx[k], j+dy[k]
                if 0<=nx<n and 0<=ny<n:
                    if room[nx][ny] in like[room[i][j]]:
                        cnt+=1
            if cnt:
                ans += 10**(cnt-1)
    return ans
print(*room,sep="\n")
print(score())

