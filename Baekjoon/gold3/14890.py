# row와 col 이 각각 길이 되고 같은 높이의 길만 갈 수 있는데,
# 경사로를 통해 높이 차이가 1이 되는 길을 갈 수 있음
# 다만 경사로의 길이가 주어졌을 때, 
# 같은 높이로 경사로를 받칠 수 없다면 경사로 설치가 불가함
# 
# 1. row 방향의 길이 지나갈 수 있는 길인지 체크 할 수 있는 check 함수 생성
# 1.1. 왼쪽에서 오른쪽 방향으로 한칸씩 이동하면서 아래를 반복함
# 1.1.1. 이전 높이와 현재 높이가 같다면, 한칸 이동하면서 경사로 설치 가능 (동일한 높이) 길이를 담는 temp에 1을 더해줌
# 1.1.2. 만약 이전 높이보다 현재 높이가 닞다면, 내리막길 이라면
#        경사로의 길이 l만큼 이동하면서 
#        만약 l칸을 다 채우지 못하고 길의 끝에 도달하거나 
#        이전 높이보다 1칸 아래 높이를 유지하지 못한다면 (더 높아지거나 낮아지거나)
#        지나갈 수 없는 길임으로 False를 반환한다
#        하지만 l을 이동하는 동안 1칸 낮은 높이를 유지했다면
#        기존 위치 i에 l을 더해주고, 경사로가 설치된 곳엔 다시 경사로를 설치할 수 없음으로 temp는 0으로 초기화 한다
# 1.1.3. 만약 이전 높이보다 현재 높이가 높다면, 오르막길 이라면
#        경사로 설치 가능 길이가 l개를 만족하는지, 이전 높이가 현재 높이보다 1칸 낮은지를 확인하여
#        둘 중 하나라도 아니라면 지나갈 수 없는 길임으로 False를 반환하고
#        만약 경사로 설치가 가능하다면 다음 칸으로 이동하고 temp는 지금 있는 자리를 포함해야 함으로 1로 초기화 한다
# 1.2. 만약 모든 길을 무사히 통과 했다면 True를 반환한다
# 
# 2. row 방향의 길을 확인하는 함수를 만들었음으로
#    처음 받은 array 를 transpose 한 arrT를 생성하고 열에 대하여도 row 방향으로 체크할 수 있도록 한다
# 3. sol 함수를 통해 0~n-1을 지나면서 arr 와 arrT의 row가 check 함수를 통과하면 길을 하나 추가하고, 
#    아니면 지나가면서 마지막에 가능한 길의 개수를 print한다 

import sys
input = sys.stdin.readline

def check(row):
    i = 1
    temp = 1
    while i < n:
        bf = row[i-1]
        if bf == row[i]:
            i += 1
            temp += 1
        elif bf > row[i]:
            for k in range(l):
                if i+k >= n or bf - 1 != row[i+k]:
                    return False
            i += l
            temp = 0
        else:
            if temp < l or bf + 1 != row[i]:
                return False
            i += 1
            temp = 1
    return True

n,l = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arrT = list(map(list,zip(*arr)))

def sol():
    road = 0
    for i in range(n):
        if check(arr[i]):
            road += 1
        if check(arrT[i]):
            road += 1
    print(road)
    return
sol()