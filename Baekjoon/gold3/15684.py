import sys
input = sys.stdin.readline
n,m,h = map(int, input().split())
bridge = [[0]*(h) for _ in range(n+1)]
for _ in range(m):
    # a: 가로선, b: 세로선
    a,b = map(int, input().split())
    bridge[b][a-1] = 1

def check():
    for i in range(1,n+1):
        col = i
        for j in range(h):
            if bridge[col][j]:
                col += 1
            elif col > 1 and bridge[col-1][j]:
                col -= 1
        if col != i:
            return False
    return True

def sol(cnt,level):
    global ans
    if cnt > 3:
        return 0
    if check():
        ans = min(ans,cnt)
        return 
    
    for j in range(level,h):
        for col in range(1,n):
            if bridge[col-1][j] or bridge[col][j] or bridge[col+1][j]:
                continue
            bridge[col][j] = 1
            sol(cnt+1,j)
            bridge[col][j] = 0

if m == 0:
    print(0)
else:
    ans = 5
    sol(0,0)
    if ans > 3:
        print(-1)
    else:
        print(ans)