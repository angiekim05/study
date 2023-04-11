n = int(input())
dice = list(map(int,input().split()))

# 1면만 가려짐으로 가장 큰 숫자만 가리면 됨
if n == 1:
    print(sum(dice)-max(dice))
# n*n*n의 정육면체를 만들면
# 3면이 보이는 주사위는 4개
# 2면이 보이는 주사위는 (8*(n-2)+4)개
# 1면이 보이는 주사위는 (5*(n-2)**2 + (n-2)*4)개
# 각 숫자에 맞개 곱해주고 합을 구하면 됨
else:
    a, b, c, d, e, f = dice
    # 면이 3개 보이는 경우 중 가장 작은 숫자
    plane3 = [a+b+c,a+b+d,a+c+e,a+d+e,f+b+c,f+b+d,f+c+e,f+d+e]
    # 면이 2개 보이는 경우 중 가장 작은 숫자
    plane2 = [a+b,a+c,a+d,a+e,b+c,b+d,b+f,c+e,c+f,d+e,d+f,e+f]
    print(min(plane3)*4 + min(plane2)*(8*(n-2)+4) + min(dice)*(4*(n-2)*(n-1) + (n-2)**2))
