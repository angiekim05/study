import sys
input = sys.stdin.readline
n,b = map(int,input().split())
matrixA = [list(map(int, input().split())) for _ in range(n)]

# 행렬곱 -> 결합법칙 성립
def mul(A,B):  
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += A[i][k] * B[k][j]
                temp[i][j] %= 1000
    return temp
    
def sol(A,b):
    if b == 1:
        # 원소가 1000일 경우 0으로 바꿔줌
        for x in range(n):
            for y in range(n):
                A[x][y] %= 1000
        return A
    # 분할해서 제일 작은 단위에부터 올라오는 걸로 생각 
    # 즉, 처음에는 A로 시작
    temp = sol(A, b//2)
    
    # 짝수면 제곱
    if b % 2 == 0:
        return mul(temp,temp)
    # 홀수면 제곱해준 것에 A를 곱함
    else:
        return mul(mul(temp,temp),A)

    ## 예시
    ## sol(A,10) -> b는 짝수 (C*C)
    ## sol(A,5) -> b는 홀수 ((B*B)*A) => C
    ## sol(A,2) -> b는 짝수 (A*A) => B
    ## sol(A,1) -> b는 1이므로 temp => A

for row in sol(matrixA,b):
    print(*row)