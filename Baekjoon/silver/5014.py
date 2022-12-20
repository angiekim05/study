from collections import deque
f,s,g,u,d = map(int, input().split())
q = deque([(s,0)])
visited = [0]*(f+1)
visited[s] = 1
while q:
    now,cnt = q.popleft()

    if now == g:
        print(cnt)
        break
    
    for ud in [u,-d]:
        next = now + ud
        if 0 < next <= f and visited[next] == 0:
            q.append((next,cnt + 1))
            visited[next] = 1
else:
    print("use the stairs")