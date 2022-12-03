# t의 단어들은 1개씩만 존재!
# 각 단어의 위치 관계가 중요함
# t를 완성해야함으로 앞 단어가 있어야지만 뒤에 단어의 존재 이유가 있음

S = input()
t = input()
dp = [0]*(len(t)+1)
# 첫번째는 비교를 위해 무한대로 추가해줌
dp[0] = float("inf")
find_idx = {a:idx for idx,a in enumerate(t)}
for s in S:
    # 만약 s가 t에 포함되는 단어이면서, 
    # t에서 s의 위치 이전 단어의 개수가 충분히 존재한다면
    # 다음 단어인 s를 추가할 수 있음
    # 만약 이전 단어의 개수가 모자라면 다음 단어를 추가 할 수 없음
    if s in find_idx and dp[find_idx[s]] > dp[find_idx[s]+1]:
        dp[find_idx[s]+1] += 1

print(dp[-1])