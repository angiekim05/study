# python에서 기본적으로 제공하는 sort 함수는 O(nlogn) 빠른 정렬방법이다.
# 내림차순으로 정렬하기 위해서는 reverse를 True로 설정해주면 된다.

import sys
input = sys.stdin.readline

n = int(input())
numbs = [int(input()) for _ in range(n)]
numbs.sort(reverse=True)
for i in range(n):
    print(numbs[i])