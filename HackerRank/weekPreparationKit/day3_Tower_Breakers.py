# 단어
# evenly divides 나누어 떨어지게 하다

# 수학 문제
# tower의 개수가 짝수거나 tower의 높이가 1이면 player2가 이기고
# 나머지는 player1이 이김

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def towerBreakers(n, m):
    # Write your code here
    if n % 2 == 0 or m == 1:
        return 2
    return 1


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
