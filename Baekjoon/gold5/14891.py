# n = 0, s = 1
# 시계방향: 1, 반시계방향: -1
# 각 톱니바퀴는 12시 방향부터 시계방향으로 정렬된 상태
gears = [input() for _ in range(4)]
t = int(input())
# 12시 방향의 idx
gear_idx = [0,0,0,0]
for _ in range(t):
    idx, clockwise = map(int,input().split())
    idx -= 1
    # 맞닿는 부분 확인
    # 왼쪽 바퀴의 2번째, 오른쪽 바퀴의 6번째 비교
    connection = [gears[0][(gear_idx[0]+2)%8]!=gears[1][(gear_idx[1]+6)%8],
                  gears[1][(gear_idx[1]+2)%8]!=gears[2][(gear_idx[2]+6)%8],
                  gears[2][(gear_idx[2]+2)%8]!=gears[3][(gear_idx[3]+6)%8]]
    
    gear_idx[idx] = (gear_idx[idx] - clockwise) % 8
    # 기준의 오른쪽 체크
    cw = clockwise
    for i in range(idx,3):
        if connection[i]:
            gear_idx[i+1] = (gear_idx[i+1] + cw) % 8
            cw *= -1
        else:
            break
    # 기준의 왼쪽 체크
    cw = clockwise
    for i in range(idx,0,-1):
        if connection[i-1]:
            gear_idx[i-1] = (gear_idx[i-1] + cw) % 8
            cw *= -1
        else:
            break
answer = 0
for i in range(4):
    if gears[i][gear_idx[i]] == "1":
        answer += 2**i
print(answer)
