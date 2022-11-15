# LIS 가장 긴 증가하는 수열
왼쪽에서 오른쪽 방향으로 오름차순으로 증가하는 부분 수열 중 가장 길이가 긴 수열
 |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
 | 10 | 40 | 20 | 50 | 30 | 40 | 60 |   
> 증가하는 부분 수열 {10,40,50,60} {10,20,50,60} {10,20,30,40,60} {40, 50, 60} 등   
> 가장 긴 증가하는 부분 수열의 길이는 {10,20,30,40,60} 5가 됨   

## LIS 알고리즘
- DP 활용
> DP에는 부분 수열의 길이가 담김
> 따라서 DP는 1로 초기화 됨 
``` python
array = [10,40,20,50,30,40,60]
n = len(array)
dp = [1] * n 
```
- 2번째부터는 앞의 값들과 하나씩 비교함
- 수열의 i-1번째 값보다 i번째 값이 큰 경우,
- i번째 증가하는 부분 수열의 길이는 i-1번째 길이 + 1이 된다.
``` python
for now in range(1,n): # 맨처음엔 무조건 자기자신 하나이기 때문에 두번째부터 시작
    for before in range(now): # 자기 자신의 앞에 있는 것들하고 비교해 나감
        # 증가하는 값이라면
        if array[before] < array[now]: 
            # 이전 길이에 now 1개를 더한 값이 더 길다면 긴 값으로 변경
            if dp[now] < dp[before] + 1: 
                dp[now] = dp[before] + 1
```
- 가장 긴 증가하는 부분 수열은 dp에서 가장 큰 값을 의미함
``` python
answer = max(dp)
```
   
### 최종 Python 코드
``` python
array = [10,40,20,50,30,40,60]
n = len(array)
dp = [1] * n 

for i in range(1,n): 
    for j in range(i): 
        if array[j] < array[i] and dp[i] < dp[j] + 1: 
                dp[i] = dp[j] + 1

answer = max(dp)
print(answer)
```