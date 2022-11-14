# 동전 개수의 최솟값 구하기
N, K = map(int, input().split()) # N 동전 개수, K 목표 금액
A = [0] * N # 동전 데이터 리스트

for i in range(N):
    A[i] = int(input())
    
count = 0

# 가치가 큰 동전부터 선택해야 개수를 최소로 구성할 수 있음
for i in range(N - 1, -1, -1): # N -1 ~ 0으로 역순으로 반복
    if A[i] <= K: # 현재 K보다 동전 가치가 작거나 같으면
        count += int(K / A[i]) # 동전 수 += 목표 금액 / 현재 동전 가치
        K = K % A[i] # 목표 금액 = 목표 금액 % 현재 동전 가치

print(count) # 누적된 동전 수 출력

# 카드 정렬하기 백준 1715번
from queue import PriorityQueue
N = int(input()) # 카드 묶음 개수
pq = PriorityQueue() # 우선순위 큐

for _ in range(N):
    date = int(input())
    pq.put(date)
    
data1 = 0
data2 = 0
sum = 0

# 자동 정렬에 따라 작은 카드 묶음 2개를 쉽게 뽑을 수 있음
while pq.qsize()>1:
    data1 = pq.get() # 2개 카드 묶음을 큐에서 뽑음
    data2 = pq.get()
    temp = data1 + data2 # 2개 카드 묶음을 합치는 데 필요한 비교 횟수를 결괏값에 더함
    sum += temp
    pq.put(temp) # 2개 카드 묶음의 합을 우선순위 큐에 다시 넣음

print(sum)

# 수를 묶어서 최댓값 만들기
from queue import PriorityQueue
N = int(input()) # 카드 묶음 개수
plusPq = PriorityQueue() # 양수 우선순위 큐
minusPq = PriorityQueue() # 음수 우선순위 큐
one = 0 # 1의 개수 카운트
zero = 0 # 0의 개수 카운트

for i in range(N): # 데이터를 4개의 그룹에 분리 저장
    data = int(input())
    if data > 1:
        plusPq.put(data * -1) # 양수 내림차순 정렬을 위해 -1을 곱하여 저장
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        minusPq.put(data)

sum = 0

# 양수 우선순위 큐 처리
while plusPq.qsize() > 1:
    first = plusPq.get() * -1
    second = plusPq.get() * -1
    sum += first * second

if plusPq.qsize() > 0: # 양수 우선순위 큐에 데이터가 남아 있으면
    sum += plusPq.get() * -1 # 해당 데이터를 결괏값에 더함

# 음수 우선순위 큐 처리
while minusPq.qsize() > 1:
    first = minusPq.get()
    second = minusPq.get()
    sum += first * second

if minusPq.qsize() > 0: # 음수 우선순위 큐에 데이터가 남아 있고, 데이터 0이 1개도 없으면
    if zero == 0:
        sum += minusPq.get()

sum += one # 숫자 1의 개수를 결괏값에 더함
print(sum)