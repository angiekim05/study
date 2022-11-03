# ASCII 문제
# Caesar cipher (암호화 방법 중 하나)
# : 알파벳을 k자리 뒤 알파벳으로 만드는 것

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here
    answer = ""
    a = ord("a")
    A = ord("A")
    for i in range(n):
        idx = ord(s[i])
        if a <= idx <= ord("z"):  # lowercase
            answer += chr(a + (idx + k - a) % 26)
        elif A <= idx <= ord("Z"):
            answer += chr(A + (idx + k - A) % 26)
        else:
            answer += s[i]
    return answer


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + "\n")

    fptr.close()
