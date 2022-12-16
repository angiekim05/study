from itertools import combinations
n = int(input())
cnt = 10
ans = []
if n <= 10: # 한자리 숫자는 모두 감소하는 수
    print(n)
else:
    for i in range(2,11):
        for j in combinations(range(10), i):
            # 2개 숫자로 만들 수 있는 모든 조합을 숫자 순서대로 나열하면 
            # 감소하는 수를 만들 수 있다
            num = sorted(list(j), reverse=True) 
            ans.append(int("".join(map(str, num))))
    ans.sort()
    if len(ans) <= n-10:
        print(-1)
    else:
        print(ans[n-10])