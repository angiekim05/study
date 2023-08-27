#https://www.codetree.ai/training-field/frequent-problems/problems/arrange-operator?&utm_source=clipboard&utm_medium=text

# 정수 갯수
n = int(input())

# 정수
Number = list(map(int, input().split()))

# 덧셈plus, 뺄셈subtract, 곱셈multiply
p,s,m = map(int, input().split())


def operate(idx,d,x):
    global min_, max_, p,s,m
    if d == n:
        min_ = min(min_, x)
        max_ = max(max_, x)
        return
    if p > 0:
        x += Number[idx]
        p -= 1
        operate(idx+1,d+1,x)
        p += 1
        x -= Number[idx]
    
    if s > 0:
        x -= Number[idx]
        s -= 1
        operate(idx+1,d+1,x)
        s += 1
        x += Number[idx]
    
    if m > 0:
        x *= Number[idx]
        m -= 1
        operate(idx+1,d+1,x)
        m += 1
        x //= Number[idx]

min_,max_ = float("INF"), -float("INF")
operate(1,1,Number[0])
print(min_,max_)
