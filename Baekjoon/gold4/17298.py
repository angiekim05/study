# 오른쪽에 있는 수 중 자기 자신 보다 크면서 제일 왼쪽에 있는 수
# 오큰수(nge)가 없으면 -1 
n = int(input())
a = list(map(int, input().split()))
stack = [] # 숫자를 담을 스택
nge = [-1] # 제일 오른쪽에 있는 수는 무조건 -1 (오른쪽 숫자가 없어서)
stack.append(a.pop()) # 제일 오른쪽에 있는 수를 임시로 담음

# 오른쪽 부터 체크
while a:
    now = a.pop() # now를 기준으로

    while stack and stack[-1] <= now: # 스택에 now보다 작은 수가 있으면 뽑아낸다 
                                    # (now 보다 왼쪽에 있는 수에겐 now 보다 작은 오른쪽에 있는 숫자는 필요 없음!)
        stack.pop()
    
    if stack: # 만약 스택에 남는 숫자가 있다면 now보다 큰 수
        nge.append(stack[-1]) # 해당 숫자가 now의 오큰수(nge)
    else:
        nge.append(-1) # 만약 안남아 있다면 now 보다 큰 수가 없는 것 -1
    
    # now보다 작은거 다 빼고 now 보다 큰수만 남은 스택에 새로운 now도 추가
    stack.append(now)

print(*nge[::-1])