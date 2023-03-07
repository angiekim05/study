x,k = map(int,input().split())
k = list(bin(k)[2:])
x = list(bin(x)[2:])
ans = ""
while k:
    if x:
        a = x.pop()
        if a == "1":
            ans += "0"
        else:
            ans += k.pop()
    else:
        ans += k.pop()

print(int("0b"+ans[::-1],2))