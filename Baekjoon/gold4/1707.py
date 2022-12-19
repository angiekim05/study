from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def sol():
    v,e = map(int,input().split())
    color = [0]*(v+1) # 칠해줄 색을 담을 곳
    g = defaultdict(list)
    # 양방향 그래프
    for _ in range(e):
        x,y = map(int,input().split())
        g[x].append(y)
        g[y].append(x)
    
    # 모든 노드 탐색
    for i in range(1,v+1):
        if color[i]: # 이미 지나온 노드면 넘어가기
            continue
        # 새로 접한 노드면 색을 칠해주고 인접한 노드들 탐색
        color[i] = 1
        
        q = deque([i])
        while q:
            now = q.popleft()
            next_color = color[now] % 2 + 1 # 다음 노드의 색 (색은 1 혹은 2)
            
            for next in g[now]:
                # 아직 방문하지 않았다면
                if not color[next]: 
                    color[next] = next_color
                    q.append(next)

                # 만약 인접 노드가 현재 노드와 같은 색이라면 이분 그래프가 아님
                elif color[next] != next_color: 
                    return "NO"

    # 끝까지 이상 없으면 아직은 이분 그래프
    return "YES"

k = int(input())
for _ in range(k):
    print(sol())