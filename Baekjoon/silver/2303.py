import sys
input = sys.stdin.readline

n = int(input())
membs = [0]*n
max_ = (0,0)
for m in range(n):   
    cards = list(map(int,input().split()))
    s = sum(cards)
    for i in range(4):
        for j in range(i+1,5):
            temp = (s-cards[i]-cards[j])%10
            if membs[m] < temp:
                membs[m] = temp

    if max_[0] <= membs[m]: # 계속 큰수로 갱신해야하기 때문에 =포함
        max_ = (membs[m],m)  

print(max_[1]+1)
