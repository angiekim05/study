# 파일 합치기3
# 우선순위큐를 사용해 가장 적은 비용끼리 합해가면 됨
import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    heapify(files)
    answer = 0
    while len(files) > 1:
        x = heappop(files)
        y = heappop(files)
        heappush(files, x+y)
        answer += x+y
    print(answer)