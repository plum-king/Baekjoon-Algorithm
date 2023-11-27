# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

n = int(input())
nums = map(int, input().split())
cnt = 0

for num in nums:
    m = 0
    if num > 1 :
        for i in range(2, num):  
            if num % i == 0:
                m += 1  
        if m == 0:
            cnt += 1  
print(cnt)