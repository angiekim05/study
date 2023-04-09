import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def comb(arr,r):
    res = []
    if r == 1:
        for i in range(len(arr)):
            res.append([arr[i]])
    if r > 1:
        for i in range(len(arr)-r+1):
            for temp in comb(arr[i+1:],r-1):
                res.append([arr[i]]+temp)
    return res

for x in comb(arr,m):
    print(*x)
    
# -------------------------------------------------
temp = []
def comb(idx):
    if len(temp) == m:
        print(*temp)
        return
    for i in range(idx,n):
        temp.append(arr[i])
        comb(i+1)
        temp.pop()
    return
comb(0)
