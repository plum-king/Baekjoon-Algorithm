import math

def solution(n):
    answer = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n // i == i and n % i ==0:
            #제곱수인 경우 순서쌍 하나
            answer+=1
            break
        if n % i == 0:
            answer+=2
    return answer