# https://www.codetree.ai/training-field/frequent-problems/problems/tree-tycoon?&utm_source=clipboard&utm_medium=text
# Runtime: 69ms
# Memory: 33MB

# 특수 영양제 : 높이 1 증가
# 초기 위치는 좌측 하단 4칸
# 이동 방향 1~8번
# 차분히 빠진게 없는지 체크해야함..!
dxdy = [0,(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]

# 특수 영양제의 이동 (격자의 끝과 끝이 연결됨)
# 현재 위치와 이동 방향, 이동 칸 수(거리)만큼 이동
def move_drug(x,y,d,p):
    return (x+(dxdy[d][0]*p))%n, (y+(dxdy[d][1]*p))%n

# 연간 성장
#1. 이동 -> move_drug
#2. 영양제 투입 즉, 높이 1 증가
def inject_drug(drug_pos,d,p): # 영양제 위치, 방향, 이동 거리
    new_pos = []
    for x,y in drug_pos:
        nx,ny = move_drug(x,y,d,p)
        arr[nx][ny] += 1
        new_pos.append((nx,ny))
    return new_pos

#3. 대각선 인접한 방향의 높이가 1이상인 리브로수가 있으면, 그 개수만큼 더 성장 (격자 내, 벗어나지x)
def grow_more(drug_pos):
    for x,y in drug_pos:
        cnt = 0
        # 이부분에서 실수함.. dx dy for 문에서 중복으로 많이 돌리는 실수 없길!
        for dx in [-1,1]:
            for dy in [-1,1]:
                nx,ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<n and arr[nx][ny]:
                    cnt += 1
        arr[x][y] += cnt

#4. 현재 영양제가 있는 곳 제외하고 높이 2이상이면 2 잘라서 해당 위치에 영양제 배치
def get_drug(drug_pos):
    drug_pos = set(drug_pos)
    new_pos = []
    for i in range(n):
        for j in range(n):
            if (i,j) in drug_pos:
                continue
            if arr[i][j] >= 2:
                arr[i][j] -= 2
                new_pos.append((i,j))
    return new_pos

# 모든 리브로수 높이의 합
def sum_height():
    res = 0
    for i in range(n):
        for j in range(n):
            res += arr[i][j]
    return res

n, year = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
drug_pos = [(n-2,0),(n-2,1),(n-1,0),(n-1,1)]
for _ in range(year):
    d,p = map(int, input().split())
    drug_pos = inject_drug(drug_pos,d,p)
    grow_more(drug_pos)
    drug_pos = get_drug(drug_pos)

print(sum_height())
