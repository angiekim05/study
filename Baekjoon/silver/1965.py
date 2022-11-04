n = int(input())
box = list(map(int, input().split()))
cnt = [1] * n
for i in range(n):
    for j in range(i - 1, -1, -1):
        # i번째 박스보다 앞에 있는 j번째 박스가
        # 더 작은 박스 이면서
        # 더 많은 상자를 담고 있다면,
        # i번째 박스는 j박스가 담고 있는 상자와 자신을
        # 포함한 개수만큼 담을 수 있다
        if box[i] > box[j] and cnt[i] < cnt[j] + 1:
            cnt[i] = cnt[j] + 1
print(max(cnt))