n=int(input())
a=list(map(int,input().split()))
a.sort()
x=int(input())
i,j,cnt=0,n-1,0
while i<j:
    print(a[i],a[j])
    if a[i]+a[j] == x:
        cnt+=1
        i+=1
    elif a[i]+a[j] < x:
        i+=1
    else:
        j-=1
print(cnt)