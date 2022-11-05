n, m = map(int, input().split())
numbs = list(map(int,input().split()))
numbs.sort()
answer = []
visited = set()

def sol(case, idx):
    s = tuple(case) # set에는 리스트가 못들어가고 튜플은 들어갈 수 있음
    if len(case) == m and s not in visited: # 중복되는 것 거름
        print(*s)
        visited.add(s)
        return
    for i in range(idx + 1, n):
        sol(case + [numbs[i]], i)
    return

for i in range(n):
    sol([numbs[i]], i)


## 위 방법 대신 조합을 사용할 수 있음 (입력&sort 동일)

# n, m = map(int, input().split())
# numbs = list(map(int,input().split()))
# numbs.sort()

# from itertools import combinations
# for i in sorted(set(combinations(numbs,m))):
#     print(*i)