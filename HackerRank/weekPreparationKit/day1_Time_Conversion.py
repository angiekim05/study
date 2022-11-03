import math
import os
import random
import re
import sys

def timeConversion(s):
    # Write your code here
    am_pm = s[-2:]
    if am_pm == "AM":
        if s[:2] == "12":
            return "00"+s[2:-2]
        return s[:-2]
    else:
        if s[:2] == "12":
            return s[:-2]
        return str(12+int(s[:2]))+s[2:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
