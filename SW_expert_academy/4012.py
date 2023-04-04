# 조합 구하기 -> 맨 처음 조합과 맨 마지막 조합이 서로 대칭됨
def comb(A,r):
    ret = []
    if r == 1:
        for i in range(len(A)):
            ret.append([A[i]])
    elif r > 1:
        for i in range(len(A)-r+1):
            for temp in comb(A[i+1:],r-1):
                ret.append([A[i]]+temp)
    return ret

# 점수 계산, 조합에서 2개 쌍을 골라 시너지 합 계산
# 조합은 작은 숫자에서 큰 숫자로 이루어짐으로 
# Sij에 Sji를 합한 뒤, Sij(i<j)만을 구해도 됨
def score(lst):
    cnt = 0
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            cnt += s[lst[i]][lst[j]]
    return cnt

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            s[i][j] += s[j][i] # 1->2와 2->1 를 합쳐줌
    
    ans = 100000000 # 큰수
    # 조합을 구함
    candidate = comb([i for i in range(n)],n//2)
    
    # 조합의 i번째와 -(i+1)번째는 서로 반대되는 번호를 가지고 있음
    for i in range(len(candidate)//2):
        a,b = score(candidate[i]),score(candidate[-(i+1)])
        ans = min(ans, abs(a-b))
        
    print(f"#{test_case}",ans)