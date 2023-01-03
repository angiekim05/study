# k 간격의 모든 부분합을 비교하여 최댓값을 구하는 문제

n, k = map(int,input().split())
t = list(map(int, input().split()))

# 누적합 활용
def prefixSum(n,k,t):
    # 누적합을 구함
    prefixSum = [0]*(n+1)
    for i in range(1,n+1):
        prefixSum[i] = prefixSum[i-1] + t[i-1]

    # 가능한 최솟값
    ans = -10000000
    # 최솟값과 비교하며 k 간격의 부분합의 최대값을 구함
    for i in range(k,n+1):
        ans = max(ans,prefixSum[i]-prefixSum[i-k])

    print(ans)
    return

# prefixSum(n,k,t)

#-----------------------------------------------
# 두 포인터 활용
def twoPointer(n,k,t):
    s = sum(t[:k])
    ans = s
    for i in range(n-k):
        s += t[k+i]-t[i] # 뒤에 새로운 값을 더하고, 맨 앞의 값을 빼줌
        ans = max(ans, s)
    
    print(ans)
    return
twoPointer(n,k,t)