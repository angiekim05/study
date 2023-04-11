# 4개 그룹이 있고 각 그룹에서 원소를 한개씩 뽑아 더해줬을 때 합이 0이 되는 경우의 수를 구하는 문제
# for문 3개를 돌면서 나머지 그룹에 해당 원소가 있는지 확인해주는 방법을 썼었지만 시간이 많이 소요됨
# for문 2개를 2번 돌면서 차를 구하는 방법으로 시간 단축을 할 수 있음
n = int(input())
d = [list(map(int,input().split())) for _ in range(4)]

# 그룹1과 그룹2를 더한 값에 대해 개수를 세어줌
count = dict()
for x in d[0]:
    for y in d[1]:
        s = x+y
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

# 그룹3과 그룹4의 합을 음수로 바꾸었을 때, 해당 값이 count에 있다면 0을 만들 수 있는 경우가 생긴다
# 이때 몇개까지 만들 수 있는지까지 체크해주면 됨
ans = 0
for x in d[2]:
    for y in d[3]:
        diff = x + y
        if -diff in count:
            ans += count[diff]
print(ans)
