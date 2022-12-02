# 양방향 그래프의 등산로가 주어짐
# a 출입구에서 출발하여 b 정상을 거쳐 다시 a 출입구로 돌아오는데
# 최대 intensity(이동시간)을 구하고
# 모든 a-b-a 의 intensity 중 가장 작은 값 v 를 구하여
# [b,v] 를 return 하는 문제
# (a에서 b로 가는데 제일 작은 intensity를 구하면 됨, 돌아오는건 반복)

from heapq import heappop, heappush
def solution(n, paths, gates, summits):
    hiking_trail = {i:[] for i in range(1,n+1)}
    for i,j,w in paths:
        hiking_trail[i].append((j,w))
        hiking_trail[j].append((i,w))

    summits = set(summits)
    min_intensity = [float("inf")] * (n+1)
    
    # 출입구 (시작점)
    route = []    
    for gate in gates:
        heappush(route, (0,gate))
        min_intensity[gate] = 0
    
    # 다익스트라 활용
    while route:
        w, x = heappop(route)

        if w > min_intensity[x]:
            continue
        if x in summits: # 정상에 오르면 멈춤
            continue
        for nx, nw in hiking_trail[x]:
            nw = max(w,nw) # 같은 루트 안에서 제일 큰 intensity를 담아야 함으로 max 값
            if nw < min_intensity[nx]: # nx에 도달하는 여러 루트 중 가장 작은 intensity를 담음
                min_intensity[nx] = nw
                heappush(route, (nw,nx))
    
    answer = [0,float("inf")]
    # sumits를 sorting하고 쭉 intensity만 비교 업데이트 해줘도 됨
    # 앞의 if문만 체크한다면 sorting보다 빠르지만
    # 다음 if문까지 체크하면 오히려 시간 추가됨
    for end in summits:
        if answer[1] > min_intensity[end]:
            answer[1] = min_intensity[end]
            answer[0] = end
        elif answer[1] == min_intensity[end] and answer[0] > end:
            answer[0] = end
    return answer
