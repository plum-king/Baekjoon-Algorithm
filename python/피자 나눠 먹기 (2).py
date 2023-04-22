def solution(n):
    answer = 0
    #최소공배수 구하기
    arrN=[] #n의 배수에 대한 리스트
    arr6=[] #6의 배수에 대한 리스트
    for i in range(1, n+1):
        arr6.append(i*6)
    for j in range(1, 7):
        arrN.append(j*n)

    t = False
    for s in range(len(arr6)):
        for m in range(len(arrN)):
            if arr6[s] == arrN[m]:
                big = arr6[s]
                t = True
                break
        if t == True:
            break

    answer = big//6
    return answer
