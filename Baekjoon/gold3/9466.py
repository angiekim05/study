# cycle이 생긴 경우에만 한 팀으로 인정
# 즉 자기 자신으로 돌아와야함으로 선택지에 자기 자신이 있어야함
# 선택지에 포함된 숫자들 부터 탐색해서 
# 사이클을 이루는 인원의 수를 전체 인원에서 뺌으로써 팀에 속하지 않는 인원 파악

import sys
input = sys.stdin.readline

def dfs(x,s,visited):
    global answer
    stack = [x] 
    visited[x] = 1
    cnt = 1 # 팀원 수
    while stack:
        cur = stack[-1] # 사이클을 이루는지 확인하기 위해 pop을 사용하지 않음
        next = s[cur] # 지목된 다음 사람
        if visited[next]: # 만약 이미 방문한 사람이라면
            if next in stack: # 이번 사이클에 포함된 사람이면
                return cnt - visited[next] + 1 # 팀원을 이룰 수 있는 인원 총 계산
            return 0 # 다른 팀에 이미 포함된 사람임으로 팀원 못함
        cnt += 1 # 다음 팀원도 세줌
        visited[next] = cnt
        stack.append(next)

def sol():
    n = int(input())
    s = [0] + list(map(int, input().split()))
    candidate = set(s) - set([0]) # 모든 인원을 탐색할 필요 없이 지목 당한 사람들 중 사이클을 만드는지 확인
    answer = n
    visited = [0]*(n+1)
    for x in candidate:
        if visited[x]:
            continue
        answer -= dfs(x,s,visited)
    print(answer)
    return

t = int(input())
for _ in range(t):
    sol()