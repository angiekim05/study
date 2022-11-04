# n 이 k 번 반복된 숫자의 super digit을 구하는 문제
# super digit은 모든 자릿수를 합하는 과정을 반복해서 한자리를 만들었을 때 나온 숫자
# ex) n = "86" , k = 2
#     super_digit(8686)   	8+6+8+6 = 28
# 	  super_digit(28) 	    2 + 8 = 10
# 	  super_digit(10)		1 + 0 = 1
# 	  super_digit(1)		= 1

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    # Write your code here
    # k배 해주기 전에 각자리 숫자를 더하고 k를 곱해줌
    x = str(sum(list(map(int, list(n)))) * k)
    # 한자리 숫자가 될때까지 각 자리수 더하는 걸 반복
    while len(x) > 1:
        x = str(sum(list(map(int, list(x)))))
    return x


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + "\n")

    fptr.close()
