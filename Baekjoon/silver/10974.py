# 1부터 N까지의 수로 이루어진 모든 순열을 찾는 문제
# N개의 숫자로 이루어진 순열을 만들면 됨
# 순열 생성을 위해선 백트래킹 방법을 쓸 수 있음
# for 문이 숫자를 순서대로 넘김으로 자동으로 모두 사전순으로 출력됨

n = int(input())
visited = [0]*(n+1)
p = []
def sol():
    if len(p) == n:
        print(*p)
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = 1
            p.append(i)
            sol()
            p.pop()
            visited[i] = 0
sol()