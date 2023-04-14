def solution(numer1, denom1, numer2, denom2):
    answer = []
    #그냥 [0]이나 [1]로 원소 추가할 수 없음! append로 원소 추가해줘야함
    answer.append(denom2 * numer1 + denom1 * numer2)
    answer.append(denom1 * denom2)
    
    #small: 두 수 중 작은 수
    small = answer[0]
    if answer[1] < answer[0]:
        small = answer[1] 
    
    #최대공약수 구해서 나누기
    gcd = 1
    
    #j까지 나눠보기 -> 이거까지만 하면 한 번 약분
    for i in range(2, small+1):
        if answer[0] % i == 0 and answer[1] % i == 0:
            # answer[0] = answer[0] / i
            # answer[1] = answer[1] / i
            #small을 업데이트를 해야되는데 .. 
            gcd = i
            
    answer[0] = answer[0] / gcd
    answer[1] = answer[1] / gcd
    
    return answer