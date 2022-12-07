import sys
input = sys.stdin.readline

# 소수 판별 (에라토스테네스의 체)
def eratos(n):
    sosu_TF = [False, False] + [True] * (n - 1)
    sosu = []

    for i in range(2, n + 1):
        if sosu_TF[i]:
            # 소수 입력 추가
            sosu.append(i)
            # i+i 부터 i 칸을 False로 바꾸는 것
            sosu_TF[i + i :: i] = [False] * ((n // i) - 1)

    return sosu

n = int(input())
sosu = eratos(n)
def two_pointer():
    cnt = 0
    i = 0
    j = 1
    sum = sosu[0]
    # i가 끝에 도달하기 전까지 sum 이 n보다 크면 1씩 증가 & sum 에서 i번째 소수 빼기
    while i < len(sosu):
        # j가 끝에 도달하기 전까지 sum 이 n보다 작으면 1씩 증가 & sum 에서 i번째 소수 더하기
        while j < len(sosu) and sum < n:
            sum += sosu[j]
            j += 1
        # sum 이 n하고 같으면 count
        if sum == n:
            cnt += 1

        sum -= sosu[i]
        i += 1
    return cnt
if sosu:
    print(two_pointer())
else:
    print(0)

