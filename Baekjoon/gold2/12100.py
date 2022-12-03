# 2048 게임 문제
# n*n 크기의 보드에서 최대 5번 이동하여 만들 수 있는 가장 큰 블록의 값을 구하는 문제

import sys
input = sys.stdin.readline

def left(arr):
    newarr = []
    merged = False
    for i in range(n):
        sub = []
        for j in range(n):
            cur = arr[i][j]
            if cur:# 0이 아니면 (블록이 있으면)
                # sub에 숫자블록이 있고 그게 현재 블록과 같은 숫자면 합치기
                # 이전에 합쳐진 숫자는 다시 합칠 수 없음
                if sub and sub[-1] == cur and not merged:
                    sub.pop()
                    sub.append(2*cur)
                    merged = True
                else:
                    sub.append(cur)
                    merged = False

        # 왼쪽으로 몰아 놓고 빈칸은 0으로 채우기
        newarr.append(sub + [0] * (n-len(sub)))
    return newarr

def right(arr):
    newarr = []
    merged = False
    for i in range(n):
        sub = []
        for j in range(n-1,-1,-1):
            cur = arr[i][j]
            if cur: 
                if sub and sub[-1] == cur and not merged:
                    sub.pop()
                    sub.append(2*cur)
                    merged = True
                else:
                    sub.append(cur)
                    merged = False
        newarr.append([0] * (n-len(sub)) + sub[::-1])
    return newarr

# 전치행렬
def transpose(arr):
    return list(map(list,zip(*arr)))

def up(arr):
    return transpose(left(transpose(arr)))

def down(arr):
    return transpose(right(transpose(arr)))

# 가장 큰 block 구하기
def max_block(arr):
    ans = 0
    for i in range(n):
        ans = max([ans]+arr[i])
    return ans

def sol(array,m):
    global ans
    if m == 5:
        ans = max(ans,max_block(array))
        return

    newarr = up(array)
    if array != newarr: # 만약 변동이 없었다면 멈추기
        sol(newarr,m+1)

    newarr = down(array)
    if array != newarr:
        sol(newarr,m+1)

    newarr = left(array)
    if array != newarr:
        sol(newarr,m+1)

    newarr = right(array)
    if array != newarr:
        sol(newarr,m+1)

n = int(input())
array = []
for i in range(n):
    a = list(map(int,input().split()))
    array.append(a)

# 현재 가장 큰 block부터 시작
ans = max_block(array)
sol(array,0)
print(ans)