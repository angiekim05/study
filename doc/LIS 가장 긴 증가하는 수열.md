# LIS 가장 긴 증가하는 수열
왼쪽에서 오른쪽 방향으로 오름차순으로 증가하는 부분 수열 중 가장 길이가 긴 수열
> | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 
> |:---:|:---:|:---:|:---:|:---:|:---:|:---:|
> | 10 | 40 | 20 | 50 | 30 | 40 | 60 |   
>   
> 증가하는 부분 수열 {10,40,50,60} {10,20,50,60} {10,20,30,40,60} {40, 50, 60} 등   
> 가장 긴 증가하는 부분 수열의 길이는 {10,20,30,40,60} 5가 됨   
- LIS 알고리즘: [DP 활용 방법(O(N**2))](#lis-알고리즘-dp-활용), [이분탐색 활용 방법(O(NlogN))](#lis-알고리즘-이분탐색-활용)

## LIS 알고리즘 (DP 활용)
### 시간복잡도: O(n**2)
- 관련 문제: [백준 11722번](https://www.acmicpc.net/problem/11722)
- DP에는 부분 수열의 길이가 담김
- 따라서 DP는 1로 초기화 됨 
### DP 초기화
``` python
array = [10,40,20,50,30,40,60]
n = len(array)
dp = [1] * n 
```
- 2번째부터는 앞의 값들과 하나씩 비교함
- 수열의 i-1번째 값보다 i번째 값이 큰 경우,
- i번째 증가하는 부분 수열의 길이는 i-1번째 길이 + 1이 된다.
### DP 업데이트
``` python
for now in range(1,n): # 맨처음엔 무조건 자기자신 하나이기 때문에 두번째부터 시작
    for before in range(now): # 자기 자신의 앞에 있는 것들하고 비교해 나감
        # 증가하는 값이라면
        if array[before] < array[now]: 
            # 이전 길이에 now 1개를 더한 값이 더 길다면 긴 값으로 변경
            if dp[now] < dp[before] + 1: 
                dp[now] = dp[before] + 1
# 가장 긴 증가하는 부분 수열은 dp에서 가장 큰 값을 의미함
answer = max(dp)
``` 
### 최종 LIS 코드 with DP
``` python
def sol(data):
    n = len(data)
    dp = [1] * n 
    for i in range(1,n): 
        for j in range(i): 
            if data[j] < data[i] and dp[i] < dp[j] + 1: 
                    dp[i] = dp[j] + 1
    return max(dp)

print(sol(data))
```

## LIS 알고리즘 (이분탐색 활용)
### 시간복잡도: O(NlogN)
- 관련 문제: [백준 11722번](https://www.acmicpc.net/problem/12015)
- lis 에는 증가하는 부분 수열이 담김
- 주어진 A 수열의 첫번째 값을 담은 lis 초기 상태
- A 수열의 두번째 값(target)부터 lis의 맨 마지막 값과 비교하여
- target이 더 크다면 추가하고,
- target이 더 작다면 이분탐색을 통해 lis 값 중 target보다 크면서 제일 작은 값을 target으로 갱신한다

### 기본 LIS 코드 with 이분탐색
``` python
def sol():
    n = int(input())
    a = list(map(int,input().split()))
    lis = [a[0]] # A 수열의 첫번째 값
    # A 수열의 두번째 값부터 LIS의 마지막 값과 비교
    for i in range(1,n):
        target = a[i]
        if lis[-1] < target: # 타겟이 더 크다면 LIS 에 추가
            lis.append(target)
        else:                # 타겟이 더 작다면 이분탐색을 통해 LIS 갱신
            idx = binary_search(target,lis)
            lis[idx] = target

    return len(lis) # 최종 LIS 길이 반환

print(sol())
```
### 이분탐색 함수
``` python
def binary_search(target,lis):
    start,end = 0,len(lis)-1 # 초기 시작점과 끝점
    while start < end:
        mid = (start + end) // 2 # 중간값

        if lis[mid] == target: # 중간값이 타겟과 같다면 중간값의 위치를 반환
            return mid

        # 타겟보다 큰 값 중 가장 작은 값의 위치는 
        # 아래와 같이 바로 전 값보다 크면서 바로 현재 값(중앙)보단 작은 위치이다
        elif lis[mid-1] < target < lis[mid]: 
            return mid

        # target이 더 작으면 왼쪽 더 탐색
        elif target < lis[mid]:
            end = mid - 1

        # target이 더 크면 오른쪽 더 탐색
        else:
            start = mid + 1

    return start # 만약 시작점과 끝점이 같다면 시작점을 반환
```
### 최종 LIS 코드 with 이분탐색
``` python
def binary_search(target,lis):
    start,end = 0,len(lis)-1
    while start < end:
        mid = (start + end) // 2 
        if lis[mid] == target:
            return mid
        elif lis[mid-1] < target < lis[mid]: 
            return mid
        elif target < lis[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start 
    
def sol():
    n = int(input())
    a = list(map(int,input().split()))
    lis = [a[0]] 
    for i in range(1,n):
        target = a[i]
        if lis[-1] < target: 
            lis.append(target)
        else:
            idx = binary_search(target,lis)
            lis[idx] = target

    return len(lis) 

print(sol())
```