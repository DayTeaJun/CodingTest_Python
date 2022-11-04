# DNA 비밀번호
checkList = [0] * 4 # 비밀번호 체크리스트
myList = [0] * 4 # 현재 상태 리스트
checkSecret = 0 # 몇 개의 문자와 관련된 개수를 충족했는지 판탄하는 변수

# 함수 정의
def myadd(c): # 문자 더하기 함수 / myList에 새로운 값을 더하고 조건에 따라 checkSecret값 업데이트
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1
            
def myremove(c): # 문자 빼기 함수 / myList에 새로운 값을 제거하고 조건에 따라 checkSecret값 업데이트
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split()) # S 문자열 크기, P 부분 문자열의 크기
Result = 0
A = list(input()) # 문자열 데이터
checkList = list(map(int, input().split())) # 데이터 받기

for i in range(4): # checkList를 탐색하여 0인 데이터의 개수만큼 checkSecret 값 증가
    if checkList[i] == 0: # 값이 0이면 비밀번호 개수가 이미 만족되었다는 뜻
        checkSecret += 1

for i in range(P): # P 범위(0 ~ P - 1)만큼 myList 및 checkSecret에 적응하고, 유효한 비밀번호인지 판단
    myadd(A[i]) 
if checkSecret == 4: # 유효한 비밀번호인지 판단하 결과 값을 업데이트
    Result += 1
    
for i in range(P, S): # 한 칸씩 이동하면서 제거되는 문자열과 새로 들어오는 문자열을 처리
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1

print(Result)

# 최솟값 찾기 1
from collections import deque
N, L = map(int, input().split()) # N 데이터의 개수, L 최솟값을 구하는 범위
mydeque = deque() # 데이터를 담을 덱 자료구조
now = list(map(int, input().split())) # 주어진 숫자 데이터를 가지는 리스트

# 새로운 값이 들어올 때마다 정렬 ㅐ신 현재 수보다 큰 값을 덱에서 제거해 시간 복잡도를 줄임
for i in range(N): # now 리스트를 탐색 (now[i]를 현재 값을 세팅)
    while mydeque and mydeque[-1][0] > now[i]: # 덱의 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거
        mydeque.pop()
    mydeque.append((now[i], i)) # 덱의 마지막 위치에 현재 값 저장
    if mydeque[0][1] <= i -L: # 덱의 1번째 위치에서부터 L의 범위를 벗어난 값(now index-L <= index)을 덱에서 제거
        mydeque.popleft()
    print(mydeque[0][0], end=' ') # 덱의 1번째 데이터 출력