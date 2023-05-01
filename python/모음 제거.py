def solution(my_string):
    answer = ''
    gather = ['a','e','i','o','u']
    for i in my_string:
        for j in gather:
            if i == j:
                my_string = my_string.replace(str(i), "")
                break
    answer = my_string
    return answer

print(solution("nice to meet you"))