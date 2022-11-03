import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
preorder = []
while True:
    try:
        node = int(input())
        preorder.append(node)
    except:
        break

# 루트보다 작으면 왼쪽 트리
# 루트보다 크면 오른쪽 트리(하위 혹은 상위 오른쪽 트리)
def postorder(left,right):
    if left > right:
        return

    root = preorder[left]
    mid = right + 1 # 루트보다 큰 값이 없을 수도 있기때문에 가장 끝 값 표시

    # 루트보다 큰 값이 있다면 멈춤
    # -> 해당 mid 전은 다 루트보다 작은 값이란 뜻 즉 왼쪽 트리
    for i in range(left+1,right+1):
        if root < preorder[i]:
            mid = i
            break
    
    # preorder[left] 는 루트이기 때문에 루트 빼고
    postorder(left+1,mid-1) # 왼쪽 트리 체크
    postorder(mid,right) # 오른쪽 트리 체크
    print(preorder[left])

postorder(0,len(preorder)-1)