a = input().strip()
b = input().strip()

def sol(a,b):
    n = len(a)
    m = len(b)
    ans = 0

    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(m):
            if a[i] == b[j]: # 만약 알파벳이 같다면
                dp[i+1][j+1] = dp[i][j] + 1 # 왼쪽 위의 dp에서 하나를 더함
                # 여기서 왼쪽 위를 살피는 이유는 a와 b의 현재 바로 앞단어가 동일한지 여부가 담기기 때문
            ans = max(ans, dp[i+1][j+1]) # 가장 큰 길이를 더해줌

    return ans

print(sol(a,b))