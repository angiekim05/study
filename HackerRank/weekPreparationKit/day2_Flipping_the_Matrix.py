import math
import os
import random
import re
import sys

def flippingMatrix(matrix):
    # Write your code here
    answer = 0
    k = 2*n-1
    for i in range(n):
        for j in range(n):
            answer += max(matrix[i][j],matrix[i][k-j],matrix[k-i][j],matrix[k-i][k-j])
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
