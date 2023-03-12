a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())

def gcd(x,y):
    while y > 0:
        x,y = y,x%y
    return x

c1 = a1*b2 + b1*a2
c2 = a2*b2

k = gcd(c1,c2)
print(c1//k,c2//k)