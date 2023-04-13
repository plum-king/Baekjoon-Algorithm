from itertools import permutations

n, m = list(map(int, input().split()))
# num = permutations(m, n) #iterable 반복 가능한 객체
arr =list(range(1, n+1))
num = list(permutations(arr, m))
print(num) #[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
for i in num:
    print(' '.join(map(str,i)))


# from itertools import permutations
# n, m = map(int, input().split())
# arr = list(range(1, n+1))
# num = list(permutations(arr, m)) # [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
# for i in num:
#     print(' '.join(map(str,i))) # join은 구분자.join() -> 구분자로 join 뒤에 있는 애들끼리 묶어줌
# # print(num)