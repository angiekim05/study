import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
temp = []
def dfs():
    if len(temp) == m:
        print(*temp)
        return

    for i in range(n):
        temp.append(arr[i])
        dfs()
        temp.pop()
    return

dfs()
