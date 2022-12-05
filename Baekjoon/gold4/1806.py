# 누적합 방법과 두포인터 방법이 있음
# 10 10
# 1 1 1 1 1 1 1 1 1 1
# 예시가 주어진다면 두포인터(n)가 누적합(n**2)보다 빠름

n,s = map(int,input().split())
a = list(map(int,input().split()))

# 누적합 방법 사용
def 누적합():
    # 누적합을 담을 dp
    dp = [0]*(n+1)
    ans = 100001 # s이상인 부분합 길이
    for j in range(1,n+1):
        dp[j] += dp[j-1] + a[j-1] # 누적합 담아주고
        for i in range(max(0,j-ans),j): # j에서 최소 부분합 길이 이전 부터 j-1까지 범위에서
            if dp[j]-dp[i] < s:         # 부분합이 s보다 작으면 더 진행해도 작을테니 멈춤
                break
            ans = min(ans,j-i)          # 부분합이 s를 넘으면 부분합의 길이를 줄여줌(업데이트)
    if ans != 100001: # 만약 부분합의 길이가 변하지 않았다면 그러한 합을 만드는 것이 불가능 했던 것임으로 0
        print(ans)
    else:
        print(0)

누적합()

# 두 포인터 방법 사용
def 두포인터():
    # 부분합, 부분수열의 시작점, 끝점
    sub, start, end = 0, 0, 0
    ans = 100001
    # 한칸씩 이동하면서 부분합을 비교
    while True:
        # 만약 부분합이 s보다 크면 부분합의 길이를 업데이트
        if sub >= s:
            ans = min(ans, end - start)
            # 시작점을 오른쪽으로 한칸 이동하면서 이전에 더해준 값은 빼주기
            sub -= a[start]
            start += 1
        else:
            # 마지막을 넘었다면 멈추기
            if end == n:
                break
            # 부분합이 s보다 작으면 끝점을 오른쪽으로 한칸이동
            sub += a[end]
            end += 1
    if ans == 100001:
        print(0)
    else:
        print(ans)

두포인터()