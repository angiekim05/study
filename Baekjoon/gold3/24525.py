string = input()
n = len(string)
dp = [[0,0] for _ in range(n+1)]
sk = []
for i in range(n):
    dp[i+1][0] += dp[i][0]
    dp[i+1][1] += dp[i][1]
    if string[i] == "S":
        dp[i+1][0] += 1
        sk.append((i,"s"))
    elif string[i] == "K":
        dp[i+1][1] += 1
        sk.append((i,"k"))
print(sk)
print(dp)
answer = 0
if dp[-1][0] + dp[-1][1] < 3:
    print(-1)
else:
    i, j = 0, n
    while i < j:
        # while k and dp[j][1] % 2 == 1:
        #     j = k.pop() + 1
        print(i,j)

        if (dp[j][0]-dp[i][0]) * 2 == dp[j][1]-dp[i][1] != 0:
            answer = max(answer,j-i)
            break
        j -= 1
    print(answer)