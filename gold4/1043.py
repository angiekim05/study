n,m = map(int,input().split())
known = set(map(int,input().split()[1:]))
parties = []
for i in range(m):
    parties.append(set(map(int,input().split()[1:])))

# 알고 있는 사람이 있는 파티의 멤버라면 이제 아는 사람
for i in range(m):
    # 진실을 들은 사람이 다시 전달할 수 있는 상황 고려해서 모든 상황 체크
    for party in parties:
        if known & party:
            known |= party

# 알고 있는 사람이 있는 파티 수를 전체에서 빼줌
for party in parties:
    if known & party:
        m -= 1

print(m)