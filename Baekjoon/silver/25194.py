# 0 ~ 6만 확인해 주면됨 (나머지가 4일때 헬스장 가능!)

import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
dp = [0]*7 # 나머지 숫자가 있는지 없는지 체크!
dp[0] = 1 # 나머지 0은 기본 셋팅 값

for a in A: # A의 요소 하나씩 꺼냄
    temp = [0]*7
    for j in range(7): 
        if dp[j]:               # 만약 j 나머지가 이미 있다면
            temp[(a+j) % 7] = 1 # 거기에 a를 더한 나머지를 구함
            temp[j] = 1         # temp에는 이전 숫자를 7로 나눈 나머지와
                                # 지금 숫자 a 와 이전 숫자를 더해 7로 나눈 나머지가 들어가게 됨
    dp = temp # 이전에 계산된 내용들과 지금 숫자와 계산해서 새롭게 생긴 나머지가 섞이지 않기 위해 분리
if dp[4]:
    print("YES")
else: 
    print("NO")
