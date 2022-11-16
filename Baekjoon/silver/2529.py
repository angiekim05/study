# 속도 측면에서 단축하자면
# 아래 코드는 모든 경우의 수를 다 탐색하지만
# 0~9 방향으로 탐색했을때 먼저 나온 숫자가 최솟값
# 9~0 방향으로 탐색했을때 먼저 나온 숫자가 최댓값으로
# 모든 탐색을 하지 않아도 됨

n = int(input())
sign = input().split()
answer = []
temp = [] # 임시의 조합을 담는 곳
visited = [0]*10 # 중복 없어야하니깐 방문확인
def sol(idx):
    if idx == n+1:
        answer.append("".join(list(map(str,temp))))
        return
    
    for i in range(10): # 문제에서 주어진 숫자 범위
        if visited[i]:
            continue
        temp.append(i)
        visited[i] = 1
        if (sign[idx-1] == "<" and temp[idx-1] < i) or (sign[idx-1] == ">" and temp[idx-1] > i):
            sol(idx+1)
        temp.pop()
        visited[i] = 0
    return

for i in range(10):
    temp.append(i)
    visited[i]=1
    sol(1)
    temp.pop()
    visited[i]=0

print(answer[-1]) # 최댓값
print(answer[0])  # 최솟값

