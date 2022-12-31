# 증가하는 (방문하지 않았던) 검은색 영역의 넓이를 세어줌
def makeBlack(x,y):
    global ans
    for i in range(10):
        for j in range(10):
            # x,y부터 총 10*10 넓이를 훑으면서 방문하지 않은 칸을 세어줌
            # 색종이가 도화지 밖으로 나가지 않아 걱정하지 않아도 됨
            if not visited[x+i][y+j]: 
                ans += 1
                visited[x+i][y+j] = 1


n = int(input())
visited = [[0]*100 for _ in range(100)]
ans = 0
for _ in range(n):
    x,y = map(int, input().split())
    makeBlack(x,y)

print(ans)