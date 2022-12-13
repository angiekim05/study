# 받은 연락처 문자열을 정렬한 뒤,
# 앞의 문자열이 뒤의 문자열의 앞자리와 같은지 비교

import sys
input = sys.stdin.readline

def sol():
    n = int(input())
    db = [input().strip() for _ in range(n)]
    db.sort()
    for j in range(n-1):
        if db[j] == db[j+1][:len(db[j])]:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    print(sol())