# 숫자 범위가 낮아서 완탐가능

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    # row 정렬
    for i in range(n):
        grid[i] = sorted(list(grid[i]))

    # col 정렬 체크
    m = len(grid[i])
    for i in range(n-1):
        for j in range(m):
            if grid[i][j] > grid[i+1][j]:
                return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
