# 칠판에 붙여진 단어들이 주어질 때, 영석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하시오.

str_list = list()

for i in range(5):
    n = input().strip()  
    str_list.append(n)

result = ""

str_len = max(len(str) for str in str_list)

for i in range(str_len):
    for j in range(5):
        if i < len(str_list[j]):
            result += str_list[j][i]
print(result)