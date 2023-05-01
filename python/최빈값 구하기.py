def solution(array):
    answer = 0
    arrayMode=[]
    if len(array) == 1:
        answer = array[0]
    else:
        for i in range(len(array)):
            arrayMode.append(0)
        #정렬
        array.sort()
        for i in range(1, len(array)):
            if array[i] == array[i-1]:
                arrayMode[i] = arrayMode[i-1]+1
        arrayM = sorted(arrayMode)
        if arrayM[-1] == arrayM[-2]:
            answer = -1
        else:
            for i in range(len(array)):
                if arrayMode[i] == arrayM[-1]:
                    answer = array[i] 
    return answer