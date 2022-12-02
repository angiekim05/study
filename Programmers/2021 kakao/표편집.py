from collections import deque
def solution(n, now, cmds):
    table = ["O"] * n

    # now 보다 위 or 아래에 삭제된 요소들
    up, down = deque(), deque()
    deleted = []
    for i in range(len(cmds)):
        cmd = cmds[i].split()
        # 아래로 이동
        if cmd[0] == "D":
            # 현재보다 x 만큼 아래로 이동
            now += int(cmd[1])
            # 아래로 이동하는 와중에 이미 삭제된 행이 있다면
            # 그 행만큼 더 아래로 가야함
            while down:
                if down[0] <= now:
                    up.append(down.popleft())
                    now += 1
                else:
                    break
        # 위로 이동
        elif cmd[0] == "U":
            now -= int(cmd[1])
            while up:
                if up[-1] >= now:
                    down.appendleft(up.pop())
                    now -= 1
                else:
                    break
        # 해당 행 삭제
        elif cmd[0] == "C":
            deleted.append(now)
            table[now] = "X"
            temp = now + 1
            # 만약 다음 요소가 삭제된 거라면 쭉 뒤로 이동
            while temp < n - 1 and table[temp] == "X":
                temp += 1
            # 만약 마지막 요소까지 삭제된 거라면 now 이전부터 앞으로 이동
            if temp == n:
                temp = now - 1
                while temp > 0 and table[temp] == "X":
                    temp -= 1
            # 이전보다 뒤에 위치한다면 up(이전)에 삭제된 요소 추가
            if temp > now: 
                up.append(now)
            else:
                down.append(now)
            now = temp
        # 이전 삭제 복구
        else:
            x = deleted.pop()
            table[x] = "O"
            if now > x:
                up.remove(x)
            else:
                down.remove(x)

    return "".join(table)

# print(solution(	8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))