# GCF
# ACDEB
# 위의 두가지 알파벳숫자를 다시 표현하면
# A = 10**4 ; C = 10**3 + 10; D = 10**2; G = 10**2; E = 10; B = 1
# 위와 같이 표현될 수 있다
# 제일 큰 숫자 순으로 정렬하고 큰 수부터 9~0 숫자를 붙여주면
# 가장 큰 합계를 만들 수 있다.

from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())

alpha = defaultdict(int)
prob = [0] * 11 # 10개의 알파벳의 각 자릿수를 합한 값이 들어가는 곳
numb = 1
for i in range(n):
    s = input().strip()
    k = len(s)
    for j in range(k):
        if not alpha[s[j]]:
            alpha[s[j]] = numb
            numb += 1
        prob[alpha[s[j]]] += 10 ** (k-j-1) # 10의x 자리가 추가됨

prob.sort(reverse=True)
print(prob)
total = 0
numb = 9
for i in range(10):
    total += prob[i] * numb
    numb -= 1
print(total)
