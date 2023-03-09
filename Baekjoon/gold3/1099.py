import sys
input = sys.stdin.readline

def check(word1,word2,n):
    cnt = 0
    for i in range(n):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt

s = " "+input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]

dp = [[1000]*(len(s)) for _ in range(len(s))]
dp[0][0] = 0

for i in range(1,len(s)+1):
    if dp[0][i-1] == 1000:
        continue
    for word in words:
        l = len(word)
        if sorted(s[i:i+l]) == sorted(word):
            dp[i+l-1][i] = min(dp[i+l-1][i],dp[0][i-1]+check(s[i:i+l],word,l))
            dp[0][i+l-1] = min(dp[0][i+l-1],dp[i+l-1][i])

print(dp[0][-1])