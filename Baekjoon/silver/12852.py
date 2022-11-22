# BFS
from collections import deque
n = int(input())
q = deque()
q.append([n,[n]])
visited = [0]*(n+1) # 처음 방문 -> 제일 적은 횟수로 도착

while q:
    x, l = q.popleft()
    
    if x == 1:
        print(len(l)-1)
        print(*l)
        break
        
    if visited[x]:
        continue
    visited[x] = 1
    
    if x % 3 == 0:
        nx = x//3
        q.append([nx,l+[nx]])

    if x % 2 == 0:
        nx = x//2
        q.append([nx,l+[nx]])
    
    nx = x-1
    q.append([nx,l+[nx]])