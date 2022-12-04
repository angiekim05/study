# 1자리 숫자로 글자가 만들어진 경우 
# 그 다음 자리 숫자까지 포함하여 한 개의 알파벳을 만드는 경우와
# 각각 두 개의 알파벳을 만는 경우가 있다.
# 반면 숫자 두 개로 한 개의 알파벳을 만든 경우
# 다음에는 1개 숫자로 알파벳을 추가하는 경우 한 가지가 있다. 
# 0은 그 자체로 알파벳을 만들 수 없고
# 1~26까지의 알파벳만 존재한다는 조건을 만족하는 경우의 수만 체크한다. 
# 1  ->  1/1  ->  1/1/1  ->  1/1/1/1
#                            1/1/1 1 
#                 1/1 1  ->  1/1 1/1
#        1 1  ->  1 1/1  ->  1 1/1/1
#                            1 1/1 1

cord = list(map(int,list(input().strip())))
n = len(cord)
# 마지막 자리 글자가 숫자 1개를 사용한 것인지 
# 2개를 사용한 것인지 분리해서 dp에 경우의 수 담기
dp = [[0,0] for _ in range(n)]
dp[0][0] = 1 # 처음에 무조건 숫자 1개로 1개 알파벳이 만들어짐
if cord[0] == 0:
    print(0) # 알파벳을 만들 수 없음. -> 0
else:
    for i in range(1,n):
        # 숫자 0이지만 10,20을 만들 수 있다면 통과 그 외에는 알파벳 만들 수 없음
        if cord[i] == 0:
            if dp[i-1][0] and cord[i-1] in [1,2]:
                dp[i][1] += dp[i-1][0]%1000000
            else:
                break
        else:
            dp[i][0] += (dp[i-1][0] + dp[i-1][1])%1000000 # 0이 아닌 1~9 숫자는 무조건 알파벳 가능
            # 10~26 사이의 숫자면 알파벳 가능
            if dp[i-1][0] and cord[i-1]*10+cord[i] <= 26:
                dp[i][1] += dp[i-1][0]%1000000
    print((dp[-1][0]+dp[-1][1])%1000000)
# print(dp)

# -------------------------------------------
# 더 간단한 방법
# 1. 현재 자리 숫자가 0이상이면 (1~9) 무조건 알파벳이므로 바로 전 dp 값을 더한다.
#    _ _ _ _ new -> _ _ _ _ 의 경우의 수를 더해줌
# 2. 이전 자리 숫자와 현재 자리 숫자가 10~26 숫자를 만든다면 전 전 dp 값을 더한다.
#    _ _ _ bf new -> _ _ _ 의 경우의 수를 더해줌

cord = list(map(int,list(input().strip())))
n = len(cord)
dp = [0] * (n+1)
if cord[0] == 0:
    print(0) # 알파벳을 만들 수 없음. -> 0
else:
    # 맨 처음에 공백을 추가함으로써 dp와 자리 맞춰줌
    cord = [0] + cord 
    # dp에 초기 경우의 수를 넣어줌 0번째는 초기 2자리 숫자 알파벳의 경우의 수, 1번째는 1자리 숫자 알파벳의 경우의 수
    dp[0] = dp[1] = 1
    for i in range(2,n+1):
        # 숫자가 1~9 사이면
        if cord[i] > 0:
            dp[i] += dp[i-1]%1000000
        # 이전 숫자까지 포함해서 10~26이면
        if 10 <= cord[i-1]*10+cord[i] <= 26:
            dp[i] += dp[i-2]%1000000
    print(dp[-1]%1000000)