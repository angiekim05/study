import sys
input = sys.stdin.readline
shortcut = set([' '])

n = int(input())
for _ in range(n):
    string = input().strip()
    s = string.split()
    for i in range(len(s)):
        if s[i][0].lower() in shortcut:
            continue
        else:
            shortcut.add(s[i][0].lower())
            s[i] = f"[{s[i][0]}]"+s[i][1:]
            print(' '.join(s))
            break
    else:
        ans = ""
        for i in range(len(string)):
            if string[i].lower() in shortcut:
                continue
            else:
                shortcut.add(string[i].lower())
                string = string[:i] + f"[{string[i]}]" + string[i+1:]
                break
        print(string)