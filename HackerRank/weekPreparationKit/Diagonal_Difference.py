import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    # Write your code here
    cnt = [0,0]
    for i in range(n):
        cnt[0] += arr[i][i]
        cnt[1] += arr[n-i-1][i]
    return abs(cnt[0]-cnt[1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
