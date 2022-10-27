n = int(input())
standard = ["  *  ",
            " * * ",
            "*****"]

def stars(n):
    if n == 3:
        return standard
    else:
        answer = stars(n//2)
        temp = []
        for i in range(n//2):
            temp.append(" "*(n//2)+answer[i]+" "*(n//2))
            answer[i] += " " + answer[i]
        return temp+answer

for x in stars(n):
    print(x)