# 문제
# 직선상에 n개의 높이가 서로 다른 탑이 있음
# 송신기는 꼭대기에 있고, 레이저는 수평 직선의 "왼쪽"으로 발사
# 수신기는 탑의 기둥 모두에 있음
# 레이저는 수신 1번만 (하나의 탑에 닿으면 사라짐)
# 각 탑이 받아들이는 레이저 수신 횟수를 return


n = int(input())
tower = list(map(int,input().split()))
answer = [0]*n
stack = []
# 앞으로 이동하니깐 맨 마지막 탑 높이부터 처음 탑으로 이동하며 비교!
for i in range(n-1,-1,-1):
        # stack은 오른쪽에 추가되는 숫자가 무조건 더 작은 숫자일 것임으로
        # 오른쪽부터 비교해서 탑의 높이보다 작다은 타워 수만큼
        # 수신한 레이저 숫자를 증가시키면 됨
    while stack and tower[i] > tower[stack[-1]]: 
        idx = stack.pop() # 스택의 맨 마지막 탑의 높이가 더 작다면 부딪힌것
        answer[idx] = i + 1

    stack.append(i) # 현재 탑에서 레이저 발사 높이(탑 높이) 입력
print(' '.join(list(map(str, answer))))