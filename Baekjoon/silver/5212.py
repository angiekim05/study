import sys
input = sys.stdin.readline
r,c = map(int, input().split())
land = [input().strip() for _ in range(r)]
row = [0]*r
col = [0]*c
dic = {".":0,"X":1}
after = [l for l in land] # 변한 지도 체크해둘 곳

for i in range(r):
    for j in range(c):
        if land[i][j] == "X":
            cnt = 0 # 주변의 땅 개수 세기
            for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                nx,ny = i+dx,j+dy
                if 0 <= nx < r and 0 <= ny < c:
                    cnt += dic[land[nx][ny]]
                
            # 잠기지 않는 땅의 왼쪽 오른쪽 위쪽 아래쪽을 파악하기 위해 땅의 인덱스를 체크해둠
            if cnt > 1: # 주변에 2개 이상의 땅이 있다면 잠기지 않는 땅
                row[i] = 1
                col[j] = 1
            else:
                after[i] = after[i][:j] + "." + after[i][j+1:]

# 제일 왼쪽/오른쪽에 있는 땅의 인덱스
left,right = col.index(1),c-col[::-1].index(1)
for i in range(row.index(1),r-row[::-1].index(1)):
    print(after[i][left:right])