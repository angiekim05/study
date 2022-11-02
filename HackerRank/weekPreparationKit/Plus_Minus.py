import math
import os
import random
import re
import sys
from decimal import Decimal
def plusMinus(arr):
    cnt = [0,0,0]
    for a in arr:
        if a > 0:
            cnt[0] += 1
        elif a < 0:
            cnt[1] += 1
        else:
            cnt[2] += 1
    
    # positive
    print(Decimal(str(cnt[0]))/Decimal(str(n)))
    # negative
    print(Decimal(str(cnt[1]))/Decimal(str(n)))
    # zero
    print(Decimal(str(cnt[2]))/Decimal(str(n)))

    return

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
