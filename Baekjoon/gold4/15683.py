# import sys
# input = sys.stdin.readline

# # 직접 시도한 코드 // 아래 dfs를 활용하여 cctv 감시 구간을 체크하는 코드 포함

# # 한방향으로 이동하면서 cctv에서 보이는 공간 표시하기
# def oneway(x,y,arr,dir):
#     if dir == "r":
#         for j in range(y+1,m):
#             if arr[x][j] == 6:
#                 break
#             elif arr[x][j] == 0:
#                 arr[x][j] = -1
#         return
#     elif dir == "l":
#         for j in range(y-1,-1,-1):
#             if arr[x][j] == 6:
#                 break
#             elif arr[x][j] == 0:
#                 arr[x][j] = -1
#         return
#     elif dir == "u":
#         for i in range(x-1,-1,-1):
#             if arr[i][y] == 6:
#                 break
#             elif arr[i][y] == 0:
#                 arr[i][y] = -1
#         return
#     elif dir == "d":
#         for i in range(x+1,n):
#             if arr[i][y] == 6:
#                 break
#             elif arr[i][y] == 0:
#                 arr[i][y] = -1
#         return

# # 한방향을 이용하여 나머지 다른 방향 cctv 시각 표시
# def twoway(x,y,arr,dir):
#     if dir == "ud":
#         oneway(x,y,arr,"u")
#         oneway(x,y,arr,"d")
#         return
#     elif dir == "lr":
#         oneway(x,y,arr,"l")
#         oneway(x,y,arr,"r")
#         return
#     elif dir == "ul":
#         oneway(x,y,arr,"u")
#         oneway(x,y,arr,"l")
#         return
#     elif dir == "ur":
#         oneway(x,y,arr,"u")
#         oneway(x,y,arr,"r")
#         return
#     elif dir == "dl":
#         oneway(x,y,arr,"d")
#         oneway(x,y,arr,"l")
#         return
#     elif dir == "dr":
#         oneway(x,y,arr,"d")
#         oneway(x,y,arr,"r")
#         return
    
# def threeway(x,y,arr,dir):
#     if dir == "udl":
#         oneway(x,y,arr,"u")
#         oneway(x,y,arr,"d")
#         oneway(x,y,arr,"l")
#         return
#     elif dir == "udr":
#         oneway(x,y,arr,"u")
#         oneway(x,y,arr,"d")
#         oneway(x,y,arr,"r")
#         return
#     elif dir == "ulr":
#         oneway(x,y,arr,"u")
#         oneway(x,y,arr,"l")
#         oneway(x,y,arr,"r")
#         return
#     elif dir == "dlr":
#         oneway(x,y,arr,"d")
#         oneway(x,y,arr,"l")
#         oneway(x,y,arr,"r")
#         return

# # 사각지대에 포함되는 공간 세기
# def count(arr):
#     cnt = 0
#     for i in range(n):
#         cnt += arr[i].count(0)
#     return cnt

# def sol(arr,cctv_idx):
#     global answer
#     # k개 cctv를 적용했을 때 사각지대 확인
#     if cctv_idx == k:
#         answer = min(answer,count(arr))
#         # print(*arr,sep="\n",end="\n\n")
#         return

#     # 다음 cctv를 위치 및 종류
#     x,y,numb = cctv[cctv_idx]

#     # cctv 종류에 따라 각 방향에서 cctv에 보이는 영역 포시하고 다음 cctv로 넘어감
#     if numb == 1:
#         for dir in list("udlr"):
#             newarr = [[arr[i][j] for j in range(m)] for i in range(n)]
#             oneway(x,y,newarr,dir)
#             sol(newarr,cctv_idx+1)
#     elif numb == 2:
#         for dir in ["ud","lr"]:
#             newarr = [[arr[i][j] for j in range(m)] for i in range(n)]
#             twoway(x,y,newarr,dir)
#             sol(newarr,cctv_idx+1)
#     elif numb == 3:
#         for dir in ["ul","ur","dl","dr"]:
#             newarr = [[arr[i][j] for j in range(m)] for i in range(n)]
#             twoway(x,y,newarr,dir)
#             sol(newarr,cctv_idx+1)
#     elif numb == 4:
#         for dir in ["udl","udr","ulr","dlr"]:
#             newarr = [[arr[i][j] for j in range(m)] for i in range(n)]
#             threeway(x,y,newarr,dir)
#             sol(newarr,cctv_idx+1)
#     elif numb == 5:
#         newarr = [[arr[i][j] for j in range(m)] for i in range(n)]
#         oneway(x,y,newarr,"u")
#         oneway(x,y,newarr,"d")
#         oneway(x,y,newarr,"l")
#         oneway(x,y,newarr,"r")
#         sol(newarr,cctv_idx+1)
#     return

# n, m = map(int, input().split())
# # 오피스 공간
# office = []
# # cctv의 위치를 따로 받음
# cctv = []
# for i in range(n):
#     temp = list(map(int,input().split()))
#     for j in range(m):
#         if 0 < temp[j] < 6: # 1~5번 cctv일 때 담음
#             cctv.append((i,j,temp[j]))
#     office.append(temp)

# # cctv 개수
# k = len(cctv)
# answer = float("inf")
# sol(office,0)
# print(answer)

#------------------------------------------------------------
# 좀 더 빠르고 간단한 방법
# dfs 사용하여 감시구간 체크 

n, m = map(int, input().split())
# 오피스 공간
office = []
# cctv의 위치를 따로 받음
cctv = []
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(m):
        if 0 < temp[j] < 6: # 1~5번 cctv일 때 담음
            cctv.append((i,j,temp[j]))
    office.append(temp)

# cctv 개수
k = len(cctv)
# 사각지대 수
answer = float("inf")

# 이동 방향 (up down left right)
dx, dy = (-1,1,0,0), (0,0,-1,1)

# cctv 번호에 따른 이동 경우의 수
# up:0, down:1, left:2, right:3
cctv_numb = [0,   # 0번은 없음
            # 1번 cctv는 up, down, left, right 각각의 방향을 감시
            [[0],[1],[2],[3]],   
            # 2번 cctv는 up&down, left&right 두 가지 경우의 수로 감시
            [[0,1],[2,3]],
            # 3번은 "ul","ur","dl","dr"
            [[0,2],[0,3],[1,2],[1,3]],
            # 4번은 "udl","udr","ulr","dlr"
            [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
            # 5번은 모든방향 한번에 감시
            [[0,1,2,3]]
            ]

# 사각지대에 포함되는 공간 세기(동일)
def count(arr):
    cnt = 0
    for i in range(n):
        cnt += arr[i].count(0)
    return cnt

def dfs(arr,cctv_idx):
    global answer
    # k개 cctv를 적용했을 때 사각지대 확인
    if cctv_idx == k:
        answer = min(answer,count(arr))
        return

    # 다음 cctv를 위치 및 종류
    x,y,numb = cctv[cctv_idx]

    # cctv 번호에 따라서 가능한 방향의 경우의 수
    for cctv_dir in cctv_numb[numb]:
        # 각 경우의 수에 따라 바꿔준 감시 구간을 다시 원상복귀 시키기 위해 위치 담아놓음
        # 새로운 arr를 만들고 변형시킬 수 있지만 이 방법이 시간 절약
        temp = []
        # 방향마다 감시 범위 체크
        # 예를 들어 1번은 한 방향만 감시, 2~5번은 여러 방향 감시 
        # -> 각 방향에 따라 감시 구간 체크
        for dir in cctv_dir: # dir -> up:0, down:1, left:2, right:3
            # 벽이 나오기 전까지 쭉 cctv 감시 가능
            nx,ny = x,y # 이동 시작 위치
            while True:
                nx+=dx[dir]
                ny+=dy[dir]
                # 벽이거나 오피스 밖이면 그만 이동
                if nx < 0 or nx >= n or ny < 0 or ny >= m or arr[nx][ny] == 6:
                    break
                if arr[nx][ny] == 0: # 빈 공간이면 감시 구간 표시
                    arr[nx][ny] = -1
                    temp.append((nx,ny))
        
        # 한 경우의 수에 따라 감시 구역을 체크했으면 다음 cctv로 넘어감
        dfs(arr,cctv_idx+1)
        # 끝났으면 다음 경우로 넘어가기 위해 원상복귀
        for i,j in temp:
            arr[i][j] = 0
    return

dfs(office,0)
print(answer)