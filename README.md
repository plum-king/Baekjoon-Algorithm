# 백준 문제 풀이

### 11.20 ~ 11.26

**[1978. 소수찾기](./수학/1987.py)**
<br>

**[2581. 소수](./수학/2581.py)**
<br>

**[5618. 공약수](./수학/5618.py)**


### 11.27 ~ 12.03

**[2609. 최대공약수와 최소공배수](./수학/2609.py)**
<br>

**[11653. 소인수분해](./수학/11653.py)**
<br>

**[1110. 더하기 사이클](./수학/1110.py)**

### 12.04 ~ 12.10

**[5347. LCM](./수학/5347.py)**
<br>

**[1181. 단어 정렬](./문자열/1181.py)**
- sort(): 리스트.sort()
    - sort(key=?): ?에 어떤 걸 기준으로 정렬할 것인지 작성 (EX) `sort(key=len)`
- strip(): 연속으로 입력 받을 때 '\n' 삭제할 수 있는 함수 (EX) `sys.stdin.readline().strip()`
- set(): 중복을 제거할 수 있는 함수 (EX) `b리스트 = list(set(a리스트))`
    - list() 없이 set만 사용하고 리스트에 저장하려고 하면 리스트 형태가 아닌    
    {'but', 'wont', 'it', 'hesitate', 'more', 'wait', 'yours', 'i', 'cannot', 'im', 'no'}   
    이와 같은 형태로 나타나게 된다.

**[1316. 그룹 단어 체커](./문자열/1316.py)**

### 12.11 ~ 12.17 

시험 이슈로 난이도 쉬운 문제 위주로 풀이

**[6550. 부분 문자열](./문자열/6550.py)**
<br>

**[11365. !밀비 급일](./문자열/11365.py)**
<br>

**[10798. 세로읽기](./문자열/10798.py)**

### 12.18 ~ 12.24 

**[2751. 수 정렬하기 2](./정렬/2751.py)**
<br>

**[2798. 블랙잭](./브루트포스/2798.py)**
<br>

**[10814. 나이순 정렬](./정렬/10814.py)**

### 01.01 ~ 01.07

**[10815. 숫자 카드](./정렬/10815.py)**
<br>

**[2231. 분해합](./브루트포스/2231.py)**
<br>

**[25305. 커트라인](./정렬/25305.py)**

### 01.08 ~ 01.14
**[9372. 상근이의 여행](./트리/9372.py)**
<br>

**[19532. 수학은 비대면강의입니다](./브루트포스/19532.py)**
<br>

**[18311. 왕복](./구현/18311.py)**

### 01.15 ~ 01.21
**[10828. 스택](./자료구조/10828.py)**
- remove(): 첫 번째 값을 삭제
- pop(): 특정 인덱스의 값을 삭제 (EX) pop(0): 가장 앞의 값 삭제, pop(-1): 가장 뒤의 값 삭제

**[10845. 큐](./자료구조/10845.py)**
<br>

**[10866. 덱](./자료구조/10866.py)**
- append(): 맨 뒤에 값을 삽입
- insert(): 맨 앞에 값을 삽입

### 01.22 ~ 01.28
**[10773. 제로](./자료구조/10773.py)**
<br>

**[2164. 카드2](./자료구조/2164.py)**
- deque 라이브러리 사용
    - import 방법: from collections import deque
    - deque 생성: `dec = deque()`
    - 사용 가능한 method: deque.append(), deque.pop(), deque.popleft() 등
        - deque.pop(): 오른쪽 인자 가져와서 삭제
        - deque.popleft(): 왼쪽 인자 가져와서 삭제
        - deque.appendleft(item): 왼쪽 끝에 item 추가 
<br>

**[1244. 스위치 켜고 끄기](./구현/1244.py)**

### 02.05 ~ 02.11
**[28278. 스택2](./자료구조/28278.py)**
<br>

**[18258. 큐2](./자료구조/18258.py)**
<br>

**[28279. 덱2](./자료구조/28279.py)**

### 02.12 ~ 02.18
**[1436. 영화감독 숌](./브루트포스/1436.py)**
<br>

**[9012. 괄호](./자료구조/9012.py)**
<br>

**[4949. 균형잡힌 세상](./자료구조/4949.py)**

### 02.19 ~ 02.25
**[5585. 거스름돈](./그리디/5585.py)**
<br>

**[2012. 등수 매기기](./그리디/2012.py)**
<br>

**[1874. 스택 수열](./자료구조/1874.py)**

### 02.26 ~ 03.03
**[1735. 분수 합](./수학/1735.py)**
<br>

**[11047. 동전 0](./그리디/11047.py)**
<br>

**[11399. ATM](./그리디/11399.py)**
