import sys
input = sys.stdin.readline

class function:
    def __init__(self, a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def fit(self, u, x):
        fx = max(self.a * (x - self.b)**2 + self.c, self.d)
        if fx != u or self.b > x:
            return 0
        return 1

a,b,c,d = map(int, input().split())
f = function(a,b,c,d)
n = int(input())
ans = 0
for _ in range(n):
    u,v = map(int, input().split())
    ans += f.fit(u,v)

print(ans)