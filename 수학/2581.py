# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

m = int(input())
n = int(input())

sum = 0
min = []

for i in range(m, n+1):
    rem = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                rem+=1
                break
        if rem == 0:
            sum+=i
            min.append(i)
        
if len(min) > 0:
    print(sum)
    print(min[0])
else:
    print(-1)
