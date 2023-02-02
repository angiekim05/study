from collections import defaultdict
import sys
input = sys.stdin.readline

def sol():
    m = int(input())
    cocktail = defaultdict(int)
    for _ in range(m):
        name, amount = input().split()
        cocktail[name] += int(amount)
    drinks = list(cocktail.keys())
    n = len(cocktail)
    for i in range(n):
        for j in range(i+1,n):
            if int(cocktail[drinks[i]]*1.618) == cocktail[drinks[j]] or int(cocktail[drinks[j]]*1.618) == cocktail[drinks[i]]:
                print("Delicious!")
                return 
    print("Not Delicious...")
    return 
sol()