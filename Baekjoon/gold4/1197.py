# 최소 신장 트리 / 최소 스패닝 트리
# 전체 요소를 연결
# Union-Find를 사용하는 크루스칼 알고리즘 활용

from collections import defaultdict
import sys
input = sys.stdin.readline

v,e = map(int, input().split())
g = []
for i in range(e):
    a,b,c = map(int, input().split())
    g.append((c,a,b))

# 간선을 최소 비용 순으로 오름차순 정렬
g.sort()
# 부모 노드 초기화
parent = list(range(v+1))

# Union-Find 알고리즘
def union(x,y):
    x = find(x)
    y = find(y)
    
    if y < x:
        parent[x] = y
    else:
        parent[y] = x
def find(x):
    if x == parent[x]: 
        return x
    
    else:
        parent[x] = find(parent[x])
    return parent[x]

answer = 0
for c, a, b in g:
    # 부모 노드가 서로 다르면 사이클이 발생하지 않음 (아직 연결 안 됨)
    if find(a) != find(b):
        union(a,b) # 최소 신장트리에 포함시킴
        answer += c

print(answer)