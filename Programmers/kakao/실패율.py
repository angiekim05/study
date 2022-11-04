# 배운 포인트 : sorted(stage_fail, key=lambda x: -stage_fail[x])
# 딕셔너리를 sorted 함수에 넣으면 key 리스트를 반환받을 수 있다!

from collections import defaultdict

# 실패율 = 스테이지에 멈춘 유저 수 / 스테이지에 도달한 유저 수 (멈춘 인원 + 지나간 인원 포함)
def solution(N, stages):
    total = len(stages)
    stage_fail = defaultdict(float)
    counts = defaultdict(int)

    # 각 스테이지에 멈춘 인원 세줌
    for i in range(total):
        counts[stages[i]] += 1

    for i in range(1, N + 1):
        # 스테이지에 도달한 유저가 없으면 실패율 0
        if total == 0:
            stage_fail[i] = 0

        # 스테이지에 도달한 유저는 앞선 스테이지들에 멈춘 유저들을 빼준 숫자
        # 스테이지를 순차적으로 확인함으로 전체 인원에서 각 counts[i]를 빼주면 됨
        else:
            stage_fail[i] = counts[i] / total
            total -= counts[i]
    ans = sorted(stage_fail, key=lambda x: -stage_fail[x])
    return ans