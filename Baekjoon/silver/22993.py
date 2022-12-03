# 문제는 준원이가 최후의 승자가 되는 것..... 준원이 외 생존자가 있으면 안 됨!!
n = int(input())
a = list(map(int, input().split()))
준원 = a[0]
# 공격력이 낮은 애들부터 공격하도록 정렬하기
a = a[1:]
a.sort()
for i in range(n-1):
    # 준원이 이기면 준원이 공격력 상승!
    if a[i] < 준원:
        준원 += a[i]
    # 준원이 이길 수 없는 상대 혹은 비겨서 생존자가 나타나면 끝
    elif a[i] >= 준원:
        print("No")
        break
else:
    print("Yes")