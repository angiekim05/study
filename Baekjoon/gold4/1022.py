import sys
input = sys.stdin.readline

r1,c1,r2,c2 = map(int,input().split())
n,m = abs(r1-r2)+1, abs(c1-c2)+1
ans = [[0]*m for _ in range(n)]
l = 1
for i in range(n):
    for j in range(m):
        if ans[i][j]:
            continue
        x,y = r1 + i, c1 + j
        if x == y == 0:
            ans[i][j] = "1"
        elif x < 0 and abs(y) <= abs(x):
            point = 4*(x**2) + 1
            idx, k = 0, abs(x-y)
            while j+idx < m and k <= abs(x*2):
                if ans[i][j+idx]:
                    continue
                ans[i][j+idx] = str(point - k)
                l = max(len(ans[i][j+idx]),l)
                idx, k = idx+1, k+1
        elif y < 0 and abs(x) <= abs(y):
            point = 4*(y**2) + 1
            idx, k = 0, abs(x-y)
            while i+idx < n and k <= abs(y*2):
                if ans[i+idx][j]:
                    continue
                ans[i+idx][j] = str(point + k)
                l = max(len(ans[i+idx][j]),l)
                idx, k = idx+1, k+1
        elif x > 0 and abs(y) <= abs(x):
            point = (2*x+1)**2
            idx, k = 0, abs(x-y)
            while j+idx < m and 0 <= k:
                if ans[i][j+idx]:
                    continue
                ans[i][j+idx] = str(point - k)
                l = max(len(ans[i][j+idx]),l)
                idx, k = idx+1, k-1
        elif y > 0 and abs(x) <= abs(y):
            point = (2*(y-1)+1)**2
            idx, k = 0, abs(x-y)
            while i+idx < n and 0 < k:
                if ans[i+idx][j]:
                    continue
                ans[i+idx][j] = str(point + k)
                l = max(len(ans[i+idx][j]),l)
                idx, k = idx+1, k-1

for i in range(n):
    for j in range(m):
        print(str(ans[i][j]).rjust(l," "),end=" ")
    print()