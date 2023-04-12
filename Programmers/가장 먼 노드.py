# 다익스트라를 통해 시작노드에서 나머지 노드까지의 최단 거리를 구해준다.
# 정렬을 통해 최단 거리 중에 가장 먼 노드들의 개수를 구한다.

from heapq import heappop,heappush
# 다익스트라
def dijkstra(n, dic):
    q = [(0, 1)]
    # visited에 노드 간 거리를 담았다. 무한으로 초기화
    visited = [float("inf")] * (n + 1)
    visited[0] = 0 # 사용 안하는 노드이기에 가장 작은 거리인 0을 담음
    visited[1] = 0 # 시작 노드도 거리 0
    while q:
        d, x = heappop(q) # 최단 거리들만 먼저 뽑음
        if visited[x] < d: # 저장된 거리보다 큰 거리가 나오면 패스
            continue
        for nx in dic[x]: # 연결된 모든 노드 인
            if visited[nx] > d+1: # 거리가 더 작으면 업데이트
                visited[nx] = d+1
                heappush(q,(d+1,nx))
    return visited


def solution(n, edge):
    # 양방향 노드를 딕셔너리에 담음 -> defaultdict로 담을 수 있음
    dic = dict()
    for a, b in edge:
        if a in dic:
            dic[a].append(b)
        else:
            dic[a] = [b]
        if b in dic:
            dic[b].append(a)
        else:
            dic[b] = [a]
    arr = dijkstra(n, dic)
    # 큰 수부터 정렬함을 통해 제일 큰 거리의 개수를 구한다.
    arr = sorted(arr,reverse=True)
    answer = 0
    for x in arr:
        if arr[0] == x:
            answer += 1
        else: # 더 작은 거리가 나오면 멈춤
            break
    return answer
