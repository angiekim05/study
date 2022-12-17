# 두 포인터를 활용하여 절대값이 최소가 되는 쌍을 구하기

n = int(input())
a = list(map(int,input().split()))
i,j = 0, n-1
l,r = a[i],a[j] # 정답 담기
bf = abs(a[i]+a[j]) # 절대값 비교를 위해 절대값 저장
while i < j:
    now = a[i] + a[j] # 현재 값 계산
    if bf > abs(now): # 절대값 비교해서 현재가 더 작으면 업데이트
        bf = abs(now)
        l,r = a[i],a[j]
    if now < 0: # 만약 현재 값이 양수면 오른쪽 포인터를 왼쪽으로 이동
        i += 1
    else:       # 현재 값이 음수이면 왼쪽 포인터를 오른쪽으로 이동
        j -= 1
print(l,r)