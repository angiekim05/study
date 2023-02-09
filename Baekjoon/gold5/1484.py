g = int(input())
i,j = 1,2
ans = False
while j < 100001:
    x = j**2 - i**2
    if x == g:
        print(j)
        ans = True
        j += 1
        i += 1
    elif x < g:
        j += 1
    else:
        i += 1
if ans == False:
    print(-1)