# 완전 탐색

# 0 ~ n-1개의 petrol pump가 있고
# 모든 펌프를 순차적으로 돌 수 있는 시작점을 찾는 문제
# 각 펌프는 가지고 있는 petrol 양과 다음 펌프까지의 거리가 주어짐
# 1 거리를 이동할 때 1 petrol 사용

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    # Write your code here
    n = len(petrolpumps)
    # 0 ~ n-1를 각각 시작점으로 잡았을 때
    for i in range(n):
        p = petrolpumps[i]
        # 첫 펌프에서 주어진 petrol을 트럭 탱크에 담고 
        # 이동 거리만큼 갈 수 있는지 체크
        if p[0] > p[1]:
            j = i + 1 # 앞으로 이동할 펌프 위치
            tank = p[0] - p[1] # 탱크에 남은 기름 실음
            while True:
                if j == i: # 한바퀴 돌았다면 i를 시작점으로 return
                    return i
                if j == n: # 끝에 도달했으면 맨 처음으로 돌아감
                    j = 0
                # 탱크 기름이 다음으로 이동하기 충분한지 체크
                if tank + petrolpumps[j][0] <= petrolpumps[j][1]:
                    break
                else: # 이동가능하다면 탱크 기름 & 위치 업데이트
                    tank += petrolpumps[j][0] - petrolpumps[j][1]
                    j += 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
