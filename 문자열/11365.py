# 똑똑한 당신은 암호가 뒤집으면 해독된다는 것을 발견했다.
# 이 암호를 해독하는 프로그램을 작성하시오.

while True:
    n = input()
    if n == 'END':
        break
    else:
        n = n[::-1]
        print(n)