import sys
input = sys.stdin.readline

def check(row):
    i = 1
    temp = 1
    while i < n:
        bf = row[i-1]
        if bf == row[i]:
            i += 1
            temp += 1
        elif bf > row[i]:
            temp = 0
            for k in range(l):
                if i+k >= n or bf - 1 != row[i+k]:
                    return False
            i += k + 1
        else:
            if temp < l or bf + 1 != row[i]:
                return False
            temp = 1
            i += 1
    return True

n,l = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arrT = list(map(list,zip(*arr)))
def sol():
    road = 0
    for i in range(n):
        if check(arr[i]):
            road += 1
        if check(arrT[i]):
            road += 1
    print(road)
    return
sol()