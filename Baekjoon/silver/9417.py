import sys
input = sys.stdin.readline

def gcd(x,y):
    while y > 0:
        x,y = y,x%y
    return x

n = int(input())
for _ in range(n):
    a = list(map(int,input().split()))
    m = len(a)
    ans = 0
    for i in range(m):
        for j in range(i+1,m):
            temp = gcd(a[i],a[j])
            if temp > ans:
                ans = temp
    print(ans)