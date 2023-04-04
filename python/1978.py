num = int(input())
numList =list(map(int, input().split()))
sum = 0
for i in range(0, num):
    numZero = 0
    if numList[i] > 1:
        for j in range(2, numList[i]):
            if numList[i] % j == 0:
               numZero += 1
        if numZero == 0:
            sum+=1 
print(sum)
