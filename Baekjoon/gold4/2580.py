import sys
input = sys.stdin.readline
board = [list(map(int,input().split())) for _ in range(9)]

# 빈칸 위치
empty = []
# 행마다 비는 숫자
row_candidate = []
# 열마다 비는 숫자
col_candidate = []
# 정사각형마다 비는 숫자
rec_candidate = [[set(list(range(1,10))) for _ in range(3)] for _ in range(3)]

for i in range(9):
    # 행 확인
    row_need = set(list(range(1,10)))
    exist = set(board[i])
    row_candidate.append(row_need - exist)

    # 열 확인
    col_need = set(list(range(1,10)))
    for j in range(9):
        col_need -= set([board[j][i]]) # i번째 열

        # 사각형 확인
        rec_candidate[i//3][j//3] -= set([board[i][j]])

        # 빈칸의 위치 확보
        if board[i][j] == 0:
            empty.append((i,j))

    col_candidate.append(col_need)

# dfs 재귀함수를 활용한 백트랙킹
def sol(idx):
    if idx == len(empty): # 마지막까지 도달하면 return
        return True
    x, y = empty[idx] # 빈칸 위치
    # 해당 위치에 들어갈 수 있는 후보 찾기
    row = row_candidate[x]
    col = col_candidate[y]
    rec = rec_candidate[x//3][y//3]
    candidate = row & col & rec
    # 후보들을 돌아가면서 테스트
    for c in list(candidate):
        board[x][y] = c # 후보 입력
        # 해당 후보는 이제 후보들에서 제외
        row_candidate[x] -= set([c])
        col_candidate[y] -= set([c])
        rec_candidate[x//3][y//3] -= set([c])
        if sol(idx+1): # 만약 끝까지 도달하면 return 해서 처음으로 돌아가기
            return True
        # 다시 넣어줌
        row_candidate[x] |= set([c])
        col_candidate[y] |= set([c])
        rec_candidate[x//3][y//3] |= set([c])
    
    return False

sol(0)  

for i in range(9):
    print(*board[i])
    

# --------------------------------------------------------
# 다른 코드 참고 
# set을 사용하여 집합을 업데이트 하면서 찾는 것보다
# 행렬 및 3*3사각 범위에 대하여 1~10이 들어갈 수 있는지 
# True False or 1 0 으로 표시해두고
# 확인하는 것이 속도가 더 빠름

import sys
input = sys.stdin.readline
board = [list(map(int,input().split())) for _ in range(9)]

# 빈칸 위치
empty = []
# 행 이미 있는 숫자
row = [[0] * 10 for _ in range(9)]
# 열 이미 있는 숫자
col = [[0] * 10 for _ in range(9)]
# 정사각형 범위에 이미 있는 숫자
rec = [[[0]  *10 for _ in range(3)] for _ in range(3)]

for x in range(9):
    for y in range(9):
        if board[x][y] == 0:
            empty.append((x,y))
        else:
            numb = board[x][y]
            row[x][numb] = 1          # x번째 행에 numb 숫자가 존재한다
            col[y][numb] = 1          # y번째 열에 numb 숫자가 존재한다
            rec[x//3][y//3][numb] = 1 # 3*3으로 묶인 9개의 칸 중
                                      # x//3 번째 행, y//3번째 열의
                                      # numb 숫자가 존재한다
# dfs 재귀함수를 활용한 백트랙킹
def sol(idx):
    if idx == len(empty): # 마지막까지 도달하면 return
        return True
    x, y = empty[idx] # 빈칸 위치
    # 1~9까지 넣어보면서 이미 있는 숫자면 넘어가고
    # 들어갈 수 있는 거면 다음 빈칸으로 이동
    for numb in range(1,10):
        # 이미 있는 숫자면 넘어감
        if row[x][numb] or col[y][numb] or rec[x//3][y//3][numb]:
            continue
        # numb가 스도쿠 퍼즐에 존재한다고 추가해줌
        row[x][numb] = col[y][numb] = rec[x//3][y//3][numb] = 1
        board[x][y] = numb
        if sol(idx+1): # 만약 끝까지 도달하면 return 해서 처음으로 돌아가도록 계속 끝내줌
            return True
        # 실패했다면 다시 숫자 빼줌
        row[x][numb] = col[y][numb] = rec[x//3][y//3][numb] = 0    
    return False

sol(0)  

for i in range(9):
    print(*board[i])