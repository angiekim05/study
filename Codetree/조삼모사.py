# https://www.codetree.ai/training-field/frequent-problems/problems/three-at-dawn-and-four-at-dusk?&utm_source=clipboard&utm_medium=text

# 일의 양 (2의 배수)
n = int(input())

# 업무 간의 상성 Pij
p = [list(map(int, input().split())) for _ in range(n)]

# 업무 강도 계산
def work_intensity(L):
    res = 0
    for i in range(n//2):
        for j in range(i+1,n//2):
            res += p[L[i]][L[j]]
            res += p[L[j]][L[i]]
    return res

def dfs(idx, d):
    global ans
    if d == n//2:
        temp2 = [i for i in range(n) if i not in temp]
        ans = min(ans, abs(work_intensity(temp)-work_intensity(temp2)))
    
    for i in range(idx+1,n):
        temp.append(i)
        dfs(i,d+1)
        temp.pop()

total = set(range(n))
temp = [0]
ans = float("INF")
dfs(0,1)
print(ans)
