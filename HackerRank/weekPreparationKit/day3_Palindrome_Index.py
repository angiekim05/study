# Palindrome(회문)
# 회문을 만들 수 있도록 제거해야하는 문자 찾기
# 이미 회문이거나 답이 없다면 -1
# 회문은 반 나눠서 한쪽 뒤집어 동일 여부 확인

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    s = s.strip() 
    n = len(s)
    mid = n//2    
    if s[:mid] == s[-mid:]:
        print(-1)
        return
        
    for i in range(mid):
        if s[i] != s[-i-1]:
            temp1,temp2 = s[i:-i-1], s[i+1:-i]
            mid = len(temp1)//2
            if temp1[:mid] == temp1[-mid:]:
                print(i)
                return
            elif temp2[:mid] == temp2[-mid:]:
                print(n-i-1)
                return
def palindromeIndex(s):
    # Write your code here
    s = s.strip() 
    n = len(s)
    mid = n//2   
    # 이미 회문인지 체크
    if s[:mid] == s[-mid:][::-1]:
        return -1
        
    for i in range(mid):
        # 문자가 서로 다르다면
        if s[i] != s[-i-1]:
            # 각각을 제외하고 회문이 되는지 확인
            temp1,temp2 = s[i:-i-1], s[i+1:n-i]            
            mid = len(temp1)//2
            if temp1[:mid] == temp1[-mid:][::-1]:
                return n-i-1
            elif temp2[:mid] == temp2[-mid:][::-1]:
                return i
            else:
                return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
