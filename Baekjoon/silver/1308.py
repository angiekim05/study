from datetime import date
yy,mm,dd = map(int,input().split())
today = date(yy,mm,dd)
yy,mm,dd = map(int,input().split())
dday = date(yy,mm,dd)

ans = dday-today

if ans.days > 365242:
    print("gg")
else:
    print(f"D-{ans.days}")