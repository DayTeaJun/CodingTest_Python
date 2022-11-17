# 소수 구하기
import math
M, N = map(int, input().split()) # M 시작 수 N 종료 수
A = [0] * (N + 1) # 소수 리스트

for i in range(2, N + 1):
    A[i] = i # 각각의 인덱스 값으로 초기화
    
for i in range(2, int(math.sqrt(N)) + 1): # 제곱근까지만 수행
    if A[i] == 0: # 소수가 아니면 넘어감
        continue
    for j in range(i + i, N + 1, i): # 배수 지우기
        A[j] = 0

for i in range(M, N + 1):
    if A[i] != 0:
        print(A[i]) # A에서 소수인 값 출력
        
# 거의 소수 구하기
import math
Min, Max = map(int, input().split()) # Min 시작 수, Max 종료 수
A = [0] * (10000001) # 소수 리스트

for i in range(2, len(A)): # 10^14의 제곱근인 10^7까지 반복
    A[i] = i # 각각의 인덱스값으로 초기화

for i in range(2, int(math.sqrt(len(A)) + 1)):
    if A[i] == 0:
        continue
    for j in range(i + i, len(A), i):
        A[j] = 0 # 소수가 아님을 표시
        
count = 0

for i in range(2, 10000001):
    if A[i] != 0: # 리스트에서 소수인 값일 때
        temp = A[i] # 현재 소수
        
        # 변수 표현 범위를 넘어갈 수 있어 이항 정리로 처리
        while A[i] <= Max / temp:
            if A[i] >= Min / temp:
                count += 1
            temp = temp * A[i]

print(count) # 정답 출력

# 소수 & 팰린드롬 수 중에서 최솟값 찾기
import math
N = int(input()) # 어떤 수
A = [0] * (10000001) # 소수 리스트

for i in range(2, len(A)):
    A[i] = i # 인덱스를 자기 값으로 초기화

for i in range(2, int(math.sqrt(len(A)) + 1)): # 리스트 길이의 제곱근까지 반복
    if A[i] == 0:
        continue
    for j in range(i + i, len(A), i):
        A[j] = 0

def isPalindrome(target): # 팰린드롬 판별 함수 구현
    temp = list(str(target)) # 숫잣값을 리스트 형태로 변환
    s = 0 # 시작
    e = len(temp) - 1 # 끝
    while (s < e):
        if temp[s] != temp[e]: # 시작과 끝 인덱스에 해당하는 값이 다르면 return 투 포인터
            return False
        s += 1
        e -= 1
    return True

i = N

while True: # N부터 값을 1씩 증가시키면서 A[i]값이 소수이면서 팰린드롬 수인지 판별
    if A[i] != 0:
        result = A[i]
        if (isPalindrome(result)): # 맞으면 반복문 종료
            print(result)
            break
    i += 1

# 제곱이 아닌 수 찾기
import math
Min, Max = map(int, input().split()) # 최솟값, 최댓값
Check = [False] * (Max - Min + 1) # 사이의 제곱수 판별 리스트

for i in range(2, int(math.sqrt(Max) + 1)):
    pow = i * i # 제곱수
    start_index = int(Min / pow)
    if Min % pow != 0:
        # 나머지가 있는 경우 1을 더해 Min보다 큰 제곱수에서 시작하도록 설정
        start_index += 1
    for j in range(start_index, int(Max / pow) + 1): # 제곱수의 배수 형태로 탐색
        Check[int((j * pow) - Min)] = True # 제곱수를 True로 변경

count = 0

for i in range(0, Max - Min + 1):
    if not Check[i]:
        count += 1 # 리스트에서 제곱이 아닌 수라면 count 증가

print(count)

# 오일러 피 함수 구현하기
import math
N = int(input()) # 소인수 표현
result = N

for p in range(2, int(math.sqrt(N)) +1):
    if N % p == 0: # 현재 값이 소인수라면
        result -= result / p # 현재 값
        while N % p == 0: # N에서 현재 소인수 내역을 제거
            N /= p
    
if N > 1: # N이 마지막 소인수일 때
    result -= result / N

print(int(result))