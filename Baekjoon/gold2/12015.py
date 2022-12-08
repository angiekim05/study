# 가장 긴 증가하는 부분 수열
# 기존에는 dp를 사용하여 배열에서 본인보다 이전의 값들을 살펴보면서 
# 현재 dp 값을 max(dp[now],dp[bf_idx]+1) 로 갱신했었다 -> O(n**2)
# 하지만 이번엔 더 큰 배열이 주어짐에 따라 시간을 단축시켜야 한다
#
# 증가하는 부분 수열을 담을 data 리스트를 정의하고 A 배열을 첫번째 값을 넣는다
# (data는 오름차순 유지)
# A 수열의 두번째 값부터 하나씩 타겟으로 잡고 
# 만약 data의 가장 마지막값(가장 큰 값)보다 타겟보다 크면 data에 추가한다 
# 먄약 타겟이 더 작은 값이라면, data에서 target이 위치할 수 있는 곳을 찾아 target보다 큰 수를 target으로 바꿔준다
# 다시말해, 이분탐색을 통해 target으로 수정될 위치를 찾아 data를 갱신해준다

# 예를 들어 A 수열 4 7 10 3 1 8 7 2 5 7 이 주어진다면,
# data는 다음과 같이 갱신될 수 있다
# [4] (초기 data) -> [4,7] -> [4,7,10] (target이 data의 마지막 값보다 큼으로 data에 추가)
# target 3은 data[-1] = 10 보다 작음으로 target이 들어갈 위치 이분 탐색 후 갱신 -> [3,7,10]
# [3,7,10] -> target 1 [1, 7, 10] -> target 8 [1, 7, 8] -> target 7 [1, 7, 8] 
# -> target 2 [1, 2, 8] -> target 5 [1, 2, 5] -> target 7 [1,2,5,7]
# 가장 긴 증가하는 부분 수열의 길이는 4가 된다 

def binary_search(target,data):
    start,end = 0,len(data)-1
    while start < end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid-1] < target < data[mid]:
            return mid
        elif target < data[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start

def sol():
    n = int(input())
    a = list(map(int,input().split()))
    data = [a[0]]
    for i in range(1,n):
        if data[-1] < a[i]:
            data.append(a[i])
        else:
            idx = binary_search(a[i],data)
            data[idx] = a[i]
    return len(data)

print(sol())