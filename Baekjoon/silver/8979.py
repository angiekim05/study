# 국가 번호와 금,은,동의 개수가 주어지고 k번호를 가진 국가의 순위를 도출하는 문제
# 공동 순위를 가진 국가들이 중복되어 존재한다는 점을 주의해야한다.
# k번째 국가의 메달 수에 대한 정보를 따로 기록해놓고, 
# 모든 국가들의 번호를 제외한 메달의 개수 정보를 medals 리스트에 담아 역순으로 정렬한다.
# 정렬된 리스트를 훑으며 k와 같은 메달 수를 찾으면 
# i가 k번째 국가보다 더 잘한 국가 수 임으로 i+1를 반환한다.

import sys
input = sys.stdin.readline
n,k = map(int,input().split())
medals = []
for _ in range(n):
    x, g, s, b = map(int,input().split())
    medals.append((g, s, b))
    if x == k:
        k = (g, s, b)
medals.sort(reverse=True)
for i in range(n):
    if medals[i] == k:
        print(i+1)
        break