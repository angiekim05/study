from collections import defaultdict
import sys
input = sys.stdin.readline

# 제일 왼쪽 노드부터 열을 차지함 즉 중위순회 방식을 쓸 수 있음
def mid(x,dep):
    global idx
    if x in tree and tree[x][0] != -1:
        mid(tree[x][0],dep+1)
    data[dep].append(idx)
    idx+=1
    if x in tree and tree[x][1] != -1:
        mid(tree[x][1],dep+1)

# 전체 노드에서 child 노드가 아닌 경우를 제외하면 root만 남을 것
def find_root():
    temp = set(range(1,n+1))
    temp -= child
    return temp.pop()

n = int(input())
tree = dict()
child = set()
for i in range(n):
    a,b,c = map(int, input().split())
    tree[a] = [b,c]
    child.add(b)
    child.add(c)

root = find_root()
data = defaultdict(list)
idx = 1
mid(root,1)
ans = [n+1,0]

# defaultdict는 계속 갱신이 되기 때문에 주의해야함
for dep in sorted(data.keys()):
    if ans[1] < data[dep][-1]-data[dep][0]+1:
        ans = [dep,data[dep][-1]-data[dep][0]+1]
print(*ans)
