import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    s,t = map(int, input().split()) 
    ans = 0
    while n > 0:
        if n % 2 == 1:
            n -= 1
            ans += s
        else:
            n //= 2
            if n*s > t:
                ans += t
            else:
                ans += n*s
    print(ans)