import sys
input = sys.stdin.readline

def check(w1,w2,l):
    cnt = 0
    for i in range(l):
        if w1[i] != w2[i]:
            cnt+=1
    return cnt

s = " "+input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]
words.sort()

dp = [[-1]*(len(s)) for _ in range(len(s))]
dp[0][0] = 0

for i in range(1,len(s)+1):
    if dp[0][i-1] == -1:
        continue
    for word in words:
        l = len(word)
        if sorted(s[i:i+l]) == sorted(word):
            if dp[i+l-1][i] == -1:
                dp[i+l-1][i] = dp[0][i-1]+check(s[i:i+l],word,l)
            else:
                dp[i+l-1][i] = min(dp[i+l-1][i],dp[0][i-1]+check(s[i:i+l],word,l))
            if dp[0][i+l-1] == -1:
                dp[0][i+l-1] = dp[i+l-1][i]
            else:
                dp[0][i+l-1] = min(dp[0][i+l-1],dp[i+l-1][i])

# print(*dp,sep="\n")
print(dp[0][-1])