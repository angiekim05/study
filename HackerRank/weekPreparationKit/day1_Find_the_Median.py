# find the median

import math
import os
import random
import re
import sys


def findMedian(arr):
    # Write your code here
    arr.sort()
    return arr[n//2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
