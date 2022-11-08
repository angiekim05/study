# 정확성과 효율정 둘다 테스트
# 주어진 알고력과 코딩력에 맞춰 모든 문제를 풀 수 있는 자격을 얻는 최단시간을 얻는 문제
# 각각은 공부를 하면 시간당 1씩 증가함
# 풀 수 있는 문제 중 하나를 풀면 해당 문제에서 주어진만큼 알고력과 코딩력 증가 
# but 문제풀이 시간이 추가됨

from heapq import heappush,heappop
def solution(alp, cop, problems):
    # 알고력,코딩력 1점을 얻기 위해선 1시간이 필요
    problems += [[0,0,1,0,1],[0,0,0,1,1]]

    # 모든 문제를 풀기 위해서 얻어야 하는 총 알고력과 코딩력
    max_alp, max_cop = 0, 0
    for p in problems:
        alp_req, cop_req, _,_,_ = p
        max_alp, max_cop = max(max_alp,alp_req), max(max_cop,cop_req)
    
    # 만약 현재 알고력과 코딩력이 max_alp, max_cop 보다 크다면 이미 다 풀 수 있다는 것!
    if alp >= max_alp and cop >= max_cop:
        return 0

    q = [(0,alp,cop)]
    visited = [[float("inf")]*(151) for _ in range(151)]
    visited[alp][cop] = 0
    while q:
        curCost, curAlp, curCop = heappop(q)

        # max_alp, max_cop에 도달하면 최소 시간 return
        if curAlp >= max_alp and curCop >= max_cop:
            return curCost
        
        # 이미 최소시간으로 들려서 풀었던 문제면 pass
        if visited[curAlp][curCop] < curCost:
            continue

        # problems = [alp_req, cop_req, alp_rwd, cop_rwd, cost]
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            # 문제를 풀어도 얻을게 없으면 pass
            if alp_rwd == 0 and cop_rwd == 0:
                continue
            # 풀 수 있는 문제인데 이전 cost보다 더 작다면 넣어주기
            if alp_req <= curAlp and cop_req <= curCop:
                next_alp, next_cop = min(curAlp + alp_rwd,150), min(curCop + cop_rwd,150)
                if visited[next_alp][next_cop] > curCost+ cost:
                    visited[next_alp][next_cop] = curCost+ cost
                    heappush(q, (curCost + cost, next_alp, next_cop))

