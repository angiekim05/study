import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = [list(map(int,list(input().strip()))) for _ in range(n)]
b = [list(map(int,list(input().strip()))) for _ in range(n)]

def flip(x,y):
    for i in range(3):
        for j in range(3):
            # 0 <-> 1로 전환 시킴
            a[x+i][y+j] = 1 - a[x+i][y+j]
def sol():
    if a == b: # 처음에 같은 경우는 바로 0 return
        return 0

    cnt = 0
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]: #만약 서로 다르면 a의 3x3을 전환시킴
                flip(i,j)
                cnt += 1

            if a == b:
                return cnt
    return -1

print(sol())
