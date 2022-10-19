import sys
input = sys.stdin.readline
t = int(input())
answer = [0,1,2,3,3,4,4,5]
for _ in range(t):
    answer = 0
    x, y = map(int,input().split())
    y -= x
    n = 0
    while True:
        # 12344321 형태를 만드는 것 이하로 끊음
        if y <= n * (n+1):
            break
        n += 1
    # 1234321 형태의 경우는 n ** 2
    if y <= n ** 2:
        print(n*2-1)
    else:
        print(n*2)

### 근의 공식을 이용한 방법 (시간이 굉장히 단축됨)
T = int(input())
for _ in range(T):
    x,y = map(int, input().split())
    d = y-x
    # 1+2+3+___+3+2+1 => 대칭일때 합 n(n+1) 공식 활용
    # 대칭을 가정
    # n**2 + n = d
    # n**2 + n - d = 0
    n = (-1 + (1 + 4*d)**0.5)/2
    N = int(n)
    r = d - N*(N+1) # 나머지
    if n == N:      # n이 정수일때 (123321)
        print(N*2)
    elif r <= N+1:  # 1 ~ N+1 까지 더했을 때 (1233211,1233221,1233321,1234321)
        print(N*2+1)
    else:
        print(N*2+2)# 12321 ~ 123321 사이에 있는 경우 (123211,123221)