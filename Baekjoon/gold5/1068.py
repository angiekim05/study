# 리프 노드의 수 구하기
# 한 노드를 제거하면 모든 자손들이 트리에서 제거됨
from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
nodes = list(map(int, input().split()))
delete = int(input())

# 부모 노드를 기준으로 자식 노드 리스트 만들기
tree = defaultdict(list)
for idx,k in enumerate(nodes):
    if k == delete or idx == delete:
        continue
    tree[k].append(idx)

# leaf 노드에 해당되는 노드 넣기
leaf = set()
q = [-1]
while q:
    x = q.pop()
    if tree[x]: # 만약 자식이 없다면 leaf 노드
        for nx in tree[x]:
            q.append(nx)
    else:
        leaf.add(x)
leaf -= set([-1]) # 시작 노드는 제외!
print(len(leaf))