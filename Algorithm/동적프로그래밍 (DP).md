# 동적프로그래밍 (DP, Dynamic Programming)
- 큰 문제를 작은 문제로 나누어 푸는 방법
- 분할 정복과는 다르게 작은 문제를 푸는데서 답이 같은 문제가 중복적으로 일어날 경우 사용
- 보통 점화식을 만들 수 있음
   
### 동적프로그래밍의 조건
1. 큰 문제는 작은 문제로 나눌 수 있고 작은 문제가 반복해서 나타남
2. 같은 문제라면 계산할 때마다 같은 답 도출
   
### 메모이제이션 (Memoization)
- 한번 풀었던 작은 문제를 다시 반복해서 풀지 않기 위해 메모해두고 필요할 때 답만 꺼내 보는 것
- 캐싱 (caching) 이라고도 함
- 메모이제이션을 통해 먼저 구한 결과를 담아 두면, 아래 피보나치 예시에서 점선으로 표시된 노드는 계산은 하지 않아도 됨
![피보나치 계산](https://user-images.githubusercontent.com/37467408/122693295-36a8bf00-d274-11eb-9936-9a1fc9062c29.PNG)

### 기존 피보나치 함수 (재귀)
``` python
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)
```

### 메모이제이션을 사용한 피보나치 함수
``` python
memo = [0] * (x+1)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 경우 그 답 사용
    if memo[x]:
        return memo[x]
    # 아니라면 새로 계산해서 답을 넣어줌
    memo[x] = fibo(x - 1) + fibo(x - 2)
    return memo[x]
```

   
## 동적프로그래밍(DP) 알고리즘
### 1. Top-down : 큰문제에서 분할해 작은문제를 푸는 방법
- 위의 피보나치 함수도 Top-down 방식
- 보통 재귀함수로 구현
- 가독성이 좋음
``` python
memo = [0] * (x+1)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if memo[x]:
        return memo[x]
    memo[x] = fibo(x - 1) + fibo(x - 2)
    return memo[x]
``` 
   

### 2. Bottom-up : 작은문제부터 차례로 풀어가는 방법
``` python
def fibo(x):
    memo = [0] * (x+1)
    memo[0] = 1
    memo[1] = 1

    for i in range(2,x+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[x]
``` 
   
### DP 관련 문제
백준 [2011번](https://www.acmicpc.net/problem/2011)
백준 [11049번](https://www.acmicpc.net/problem/11049)
