from collections import deque
n,k = map(int,input().split())
visited = [-1] * 100001
# n->n까지는 안움직여도 됨
visited[n] = 0
# x까지 방문 횟수
cnt = [0] * 100001
cnt[n] = 1 # n으로 시작하는데 n까지 한번 방문
# bfs
q = deque([n])
while q:
    x = q.popleft()

    for nx in [x-1,x+1,x*2]:
        if nx < 0 or nx > 100000:
            continue
        # 처음 방문 == bfs임으로 제일 최단 시간/거리
        # 즉 최초 방문일때만 갱신
        if visited[nx] == -1:
            visited[nx] = visited[x]+1
            cnt[nx] = cnt[x]
            q.append(nx) 
        # 최초 방문은 아니지만 nx에 오기까지 걸린 거리(횟수)가 같은 경우
        # 예를 들어 i까지 최단거리로 오는데 2가지 방법가 있고
        # j까지 최단거리로 오는데 이미 2가지 방법이 있었다면
        # k까지 가는 거리가 i,j가 같다면 총 2+2 방법이 있는 것
        # i->k 가 이미 더해져 있을때 j->k방법만 더하면 됨으로 다음 공식 성립
        elif visited[nx] == visited[x]+1:
            cnt[nx] += cnt[x]

print(visited[k])
print(cnt[k])