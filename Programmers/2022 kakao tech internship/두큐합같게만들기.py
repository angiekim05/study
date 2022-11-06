# 순차적으로 앞에서 뽑고 다음 큐의 뒤로 넣기 때문에
# 두 큐가 일렬로 있을 때와 같음
# 합이 같아지는 부분 즉, 전체 합의 절반(타겟)을 만드는 부분을 찾으면 됨
# 큐1을 기준으로 하나를 더해 주거나 빼줌
# 느낀점: 너무 복잡하게 생각하지 말기! 기준을 세우고 단순화 해보기

def solution(queue1, queue2):
    q = queue1 + queue2
    s,n = sum(q), len(q)
    
    # 두 큐의 합이 2로 나누어 떨어지지 않으면 
    # 같은 합이 되는 2개의 큐로 만들 수 없음
    if s % 2 != 0:
        return -1
    
    target = s // 2
    now = sum(queue1)
    # 추출할 요소의 인덱스와 집어넣을 요소의 인덱스
    idx_pop, idx_insert = 0, len(queue1)
    cnt = 0
    
    while idx_pop < n and idx_insert < n:
        # 타겟을 만족하면 끝
        if now == target:
            return cnt
        # 타겟보다 현 합계가 작으면서 집어넣을 요소가 있을 때,
        elif now < target and idx_insert < n:
            now += q[idx_insert] # 새로운 요소 추가
            idx_insert += 1 # 다음 새로운 요소 위치
        else: # 타겟보다 크면 앞에 하나 빼줌
            now -= q[idx_pop] # 추출할 요소 합계에서 제거
            idx_pop += 1 # 다음 추출될 요소
        cnt += 1 # 작업 행동 1번 추가
        
    return -1


                
            
print(solution(	[1, 2, 1, 2], [1, 10, 1, 2]))