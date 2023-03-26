import sys
from collections import Counter
input = sys.stdin.readline

def sorting(a):
    temp = []
    n,m = len(a),0
    for i in range(n):
        t = []
        for item in set(a[i]):
            if item == 0:
                continue
            c = a[i].count(item)
            t.append((item,c))
        t.sort(key=lambda x : (x[1],x[0]))
        t = [x for pair in t for x in pair]
        temp.append(t[:50])
        m = max(m,len(t))

    # 빈자리 0으로 채우기
    for i in range(n):
        if len(temp[i]) < m:
            temp[i] += [0]*(m-len(temp[i]))
            temp[i] = temp[i]
    return temp,n,m

r,c,k = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(3)]
n,m = 3,3
for s in range(101):
    if r <= n and c <= m and a[r-1][c-1] == k:
        print(s)
        break
    if n >= m:
        a,n,m = sorting(a)
    else:
        a = list(map(list,zip(*a)))
        a,m,n = sorting(a)
        a = list(map(list,zip(*a)))
else:
    print(-1)