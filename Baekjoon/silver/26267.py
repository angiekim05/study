# 직선상에 은행이 일렬로 정렬되어 있고,
# 시작 위치는 안 정해짐
# 움직이는 동안 좌표는 증가! (멈출수없음)
# 좌표 한칸 이동에 시간 1 증가
# 시간은 0부터 증가
# 시간은 거리에 따라 증가함으로 시간 t에 현재위치 x를 빼주면 
# 시간의 흐름에 따라 만날 수 있는 지점들만 비용을 더해줄 수 있음
# 최대 비용을 구하면 됨

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
cost = defaultdict(int)
for i in range(n):
    x,t,c = map(int, input().split())
    cost[t-x] += c
print(max(cost.values()))
