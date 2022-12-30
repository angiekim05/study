# 괄호의 짝이 맞으면 빼주는 방식으로 풀이
# 
from collections import deque
s = deque(list(input()))

stack = []
ans = 0
tmp = 1

while s:
    # 앞에서부터 요소를 뽑아냄
    x = s.popleft()
    
    # 앞에서부터 확인함으로 여는 괄호일때 stack에 담음
    # () 이면 2
    if x == "(":
        stack.append(x)

    # 여는 괄호일때, stack에 쌓아둔 것의 맨 뒤에 괄호와 짝이 맞으면 빼주기
    elif x in [")","]"]:
        if x+stack[-1] == "[]":
            stack.pop()
            ans 
        else:
            break

for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
        tmp *= 2

    elif s[i] == "[":
        stack.append(s[i])
        tmp *= 3

    elif s[i] == ")":
        if not stack or stack[-1] == "[":
            ans = 0
            break
        if s[i-1] == "(":
            ans += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            ans = 0
            break
        if s[i-1] == "[":
            ans += tmp

        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(ans)