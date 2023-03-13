# 최대공약수
# 유클리드 호제법

a,b = map(int,input().split())
while b > 0:
    a,b = b,a%b

print("1"*a)