import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    s = sum(arr)
    print(s-arr[-1],s-arr[0])

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
