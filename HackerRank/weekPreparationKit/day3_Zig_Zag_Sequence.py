# 단어
# permute 변환하다
# lexicographical order 사전식 순서
# 3가지 수정하기


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1) / 2) - 1  # 중앙값
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2  # 마지막은 교환했으니깐 그전꺼
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1  # 점점 줄어야함

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=" ")
    return


test_cases = int(input())
for cs in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
