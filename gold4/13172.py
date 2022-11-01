import sys
input = sys.stdin.readline
# a * b**(-1) mod x
# b**(-1) = b ** (x-2) (mod x)
# Q = 7/3 = 7 * 3**(-1) = 7 * (3**(11-2) mod 11) 
#   = 7 * 4 (mod 11) = 6 (mod 11)
X = 1000000007
m = int(input())
answer = 0
for _ in range(m):
    n,s = map(int, input().split())
    # x-2 가 매우 큰 숫자 임으로 분할 정복
    # q = s/n = (s * (n ** (x - 2) % x)) % x
    
    # 분할 정복을 사용한 거듭제곱
    def mul(n,x):
        if x == 0:
            return 1
        if x == 1:
            return n % X
        if x % 2 == 0:
            a = mul(n,x//2)
            return (a*a) % X
        else:            
            a = mul(n,x//2)
            return (n * a * a) % X

    q = s * mul(n,X-2)
    answer += q % X
print(answer % X)