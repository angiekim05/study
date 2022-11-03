import math
import os
import random
import re
import sys

def lonelyinteger(a):
    # Write your code here
    unique = set()
    for i in range(n):
        if a[i] in unique:
            unique -= set([a[i]])
        else:
            unique |= set([a[i]])

    return unique.pop()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
