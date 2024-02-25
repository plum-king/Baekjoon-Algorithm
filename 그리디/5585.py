import sys

n = 1000 - int(sys.stdin.readline())
coins = (500,100,50,10,5,1)
count = 0
for coin in coins:
    count += n//coin
    n%=coin
print(count)