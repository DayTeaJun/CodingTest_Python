# 숫자의 합 구하기
n = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum = sum + int(i) # numbers에 있는 각 자리 수를 가져와 더하기.

print(sum)

# 평균 구하기
n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)

print(sum * 100 / mymax / int(n))

# 구간 합 구하기
import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split()) # suNo = 숫자 개수, quizNo = 질의 개수
numbers = list(map(int, input().split())) # 변수 숫자 데이터 저장
prefix_sum = [0] # 합 배열 변수 선언
temp = 0

for i in numbers: # 숫자 데이터 차례대로 탐색
    temp = temp + i
    prefix_sum.append(temp) # 합 배열에 저장
    
for i in range(quizNo): # 질의 개수 만큼 반복
    s, e = map(int, input().split()) # 질의 범위 받기 (s ~ e)
    print(prefix_sum[e] - prefix_sum[s-1]) # 구간 합 출력

# 2차원 구간 합 배열
import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # n = 리스트 크기, m = 질의 수
A = [[0] * (n + 1)] # 원본 리스트
D = [[0] * (n + 1) for _ in range(n + 1)] # 합 배열

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)
    # 원본 리스트 데이터 저장
    
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 합 배열 구하기
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
        # 합 배열 저장
        
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 구간 합 배열로 질의에 답변
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)

# 나머지 합 구하기
import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # n = 수열의 개수, m = 나누어떨어져야 하는 수
A = list(map(int, input().split())) # A = 원본 수열 저장 리스트
S = [0] * n # 합 배열
C = [0] * m # 같은 나머지의 인덱스를 카운트하는 리스트
S[0] = A[0]
answer = 0 # 정답 변수

for i in range(1,n):
    S[i] = S[i-1] + A[i]
    # 합배열 저장

for i in range(n):
    remainder = S[i] % m # 합 배열에 모든 값에 % 연산
    if remainder == 0: # 0 ~ i까지의 구간 합 자체가 0일 때 정답에 더하기
        answer += 1
    C[remainder] += 1 # 나머지가 같은 인덱스의 개수 값 증가 시키기
    
    
for i in range(m): # 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2) # / 연산은 anwser 변수가 float이 되기 때문에 // 연산을 한다
        
print(answer)
