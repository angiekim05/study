# 괄호의 짝이 맞으면 빼주는 방식으로 풀이
# (()()) 의 경우, 2*(2+2) 가 되어야함 즉 4 + 4 = 8
# temp 에 2가 두번 곱해지고 세번째에 닫는 괄호를 만남
# 그럼 temp = 4 를 ans에 더하고, temp //= 2를 해줌
# 이후 다시 여는 괄호를 만나면서 2가 temp 에 곱해짐 
# 닫는 괄호를 만나면서 이를 ans에 더해주고 끝남

s = list(input())

stack = []
ans = 0
temp = 1

for i in range(len(s)):
    # 앞에서부터 요소를 뽑아냄
    x = s[i]
    
    # 앞에서부터 확인함으로 여는 괄호일때 stack에 담음
    # 여는 괄호라는 것은 (x) 2×값(X) 혹은 [x] 3*값[x] 으로 계산됨으로
    # 담을 때, 임시 값에 2 혹은 3을 곱해줌
    if x == "(":
        stack.append(x)
        temp *= 2
    elif x == "[":
        stack.append(x)
        temp *= 3

    # 닫는 괄호일때, stack에 쌓아둔 것의 맨 뒤에 괄호와 짝이 맞으면 stack에서 빼줌
    # 짝이 맞는 다는 것은 () == 2, [] == 3 의 값이 된다는 것
    # 해당 값은 이미 여는 괄호가 입력될때 temp 에 곱해졌음으로
    # 문을 닫으면서 해당 값을 ans에 더해주고 나눠줘야함
    # 이때 (()) 괄호 밖의 괄호였을 경우에는 ans에 더해주지 않음
    elif x == ")":
        if not stack or stack[-1] == "[":
            ans = 0
            break
        elif s[i-1] == "(": #괄호 안의 괄호 즉 (), [] 인 경우만 ans에 더해줌
            ans += temp
        stack.pop()
        temp //= 2

    elif x == "]":
        if not stack or stack[-1] == "(":
            ans = 0
            break
        elif s[i-1] == "[":
            ans += temp
        stack.pop()
        temp //= 3
if stack: # 뒤에 더 괄호가 있어야 하는데 더이상 맞출 짝이 없는 경우 틀린 괄호열
    print(0)
else:
    print(ans)