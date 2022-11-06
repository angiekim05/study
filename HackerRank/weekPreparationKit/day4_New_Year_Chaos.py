# 완전탐색
# 1 ~ n까지 번호 스티커가 주어지고
# 뇌물을 줘서 앞으로 한칸씩 이동가능
# 한 사람이 2칸보다 많이 이동한 경우 Too chaotic
# 사람들이 2칸 이하로 이동했을 때 모든 이동 횟수를 합한 값 return

import math
import os
import random
import re
import sys
from collections import deque
#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    # 각 사람들이 2칸 이하로 이동했는지 체크 아니라면 chaotic 반환
    for i in range(n):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
    
    target = list(range(1,n+1))
    cnt = 0
    idx = 0
    # 모두 둘러보면서 뒤에 스티커가 더 작으면 자리 바꿈
    # 총 자리 바꿈 횟수 == 이동 횟수 반환
    while q != target:
        for i in range(idx,n-1):
            if q[i] > q[i+1]:
                q[i], q[i+1] = q[i+1], q[i]
                cnt += 1
    print(cnt)
            
                

# if __name__ == '__main__':
#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         q = list(map(int, input().rstrip().split()))

#         minimumBribes(q)
n = 8
q = list(map(int, '1 2 5 3 7 8 6 4'.split()))

minimumBribes(q)
