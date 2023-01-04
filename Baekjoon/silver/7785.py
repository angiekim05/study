# 출입 기록을 통해 현재 회사에 있는 사람의 이름 사전 역순으로 출력하는 문제
# enter 이면 현재 회사에 들어왔음으로 추가
# leave 면 떠났음으로 제외를 해야함
# 중복되는 이름이 없음으로 집합으로 관리가능

import sys
input = sys.stdin.readline

n = int(input())
now = set() # 현재 회사에 있는 사람들
for _ in range(n):
    name, state = input().split() # 이름과 현재 상태
    if state == "enter":
        now.add(name)
    else:
        now -= set([name])
for name in sorted(now, reverse=True):
    print(name)