# 직선상에 각각의 집의 좌표가 주어졌을 때, 가장 인접한 두 공유기 사이의 최대 거리
# 이진 탐색을 사용하여 공유기 개수를 만족하는 최대 거리를 구하는 문제
# 이진 탐색은 원래 배열(리스트)에서 특정 값의 인덱스를 찾는 알고리즘이지만
# (중간값을 기준으로 up&down 해서 범위를 좁혀 답 구하는 것)
# 여기에서는 거리를 범위로 두고 (최소 거리 1 ~ 최대 거리 맨마지막 좌표 - 맨첫번째 좌표)
# 조건에 따라 거리의 범위를 좁혀나감
# 여기서 조건은 첫번째 집부터 x이상 떨어져 있는 집에 공유기를 설치한다고 가정했을 때
# 공유기의 수가 목표 공유기의 수보다 크면 거리를 넓히고
# 작으면 거리를 좁히는 방향으로 거리 범위를 좁혀나가는 것

import sys
input = sys.stdin.readline
n,c = map(int, input().split())
houses = [int(input()) for i in range(n)]
houses.sort()

# 최소 거리
start = 1
# 최대 거리
end = houses[-1] - houses[0]

# 이진 탐색
while start <= end:
    # mid 는 가능한 거리 범위의 중간값 -> 공유기 사이의 임시 거리
    mid = (start + end) // 2
    # 임시 거리에 대하여 몇개의 공유기를 설치할 수 있는지 확인
    # 이전 집의 위치
    bf = houses[0]
    cnt = 1 # 첫번째 집에 설치
    for i in range(1,n):
        # 집의 위치가 이전 집에서 임시 거리이상 떨어져 있다면 공유기 설치
        if houses[i] >= bf + mid: 
            cnt += 1
            bf = houses[i] # 다음 집까지의 거리를 위해 update

        # 만약 집이 목표 공유기 수를 만족한다면 거리를 더 넓혀볼 수 있음
        if cnt == c:
            start = mid + 1
            break
    # 만약 목표 공유기 수에 도달하지 못했다면 거리를 더 좁혀야 함
    else:
        end = mid - 1
print(end)