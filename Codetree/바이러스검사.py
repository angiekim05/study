# https://www.codetree.ai/training-field/frequent-problems/problems/virus-detector?&utm_source=clipboard&utm_medium=text

# 식당수
n = int(input())

# 고객수
arr = list(map(int, input().split()))

# 팀장 담당, 팀원 담당
h, t = map(int, input().split())

ans = 0

for i in range(n):
    rest = arr[i] - h
    ans += 1
    if rest > 0:
        ans += rest//t
        if rest%t > 0:
            ans += 1
          
print(ans)
