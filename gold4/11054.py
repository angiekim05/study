from binascii import a2b_base64


n = int(input())
a1 = list(map(int, input().split()))
a2 = a1[::-1] # a1 뒤집기

asc = [1]*n # 가장 긴 증가하는 부분 수열 개수 담을 리스트
desc = [0]*n # 가장 긴 감소하는 부분 수열 개수 담을 리스트
# 나중에 두개 합함 -> 자기 자신은 한번만 더하면 되니깐 하나는 1 하나는 0

for i in range(n):
    # i 이전 숫자들 체크
    for j in range(i):
        # 기준 숫자보다 작은 숫자면
        if a1[i] > a1[j]:
            # 기준 숫자의 가장 긴 증가하는 부분 수열 개수와
            # j일 때까지의 가장 긴 증가하는 부분 수열의 개수 + 1을 비교
            asc[i] = max(asc[i],asc[j]+1)
        # 위와 같이 a1을 뒤집어 가장 긴 증가하는 부분 수열을 구함
        # 즉 가장 긴 감소하는 부분 수열을 구하는 것과 같음
        if a2[i] > a2[j]:
            desc[i] = max(desc[i],desc[j]+1)

# 가장 긴 증가하는 부분 수열 길이와 
# 가장 긴 감소하는 부분 수열의 길이를 
# 합해서 가장 긴 바이토닉 수열 찾기
answer = 0
for i in range(n):
    answer = max(answer,asc[i]+desc[(n-1)-i])

print(answer)

#lis(최장 증가 부분수열) 문제 11053번 11055번 11722번 12015번 12738번 14002번 14003번