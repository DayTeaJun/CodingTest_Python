# 원하는 정수 찾기
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input()) # 탐색할 숫자 개수 저장
target_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = target_list[i] # 찾아야 하는 수
    # 이진 탐색 시작
    start = 0
    end = len(A) - 1
    while start <= end:
        midi = int((start + end) / 2) # 중간 인덱스
        midv = A[midi] # 중앙값
        if midv > target: 
            end = midi - 1
        elif midv < target:
            start = midi + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)
        
# 블루레이 만들기
N, M = map(int, input().split()) # N 레슨 개수, M 블루레이 개수
A = list(map(int, input().split())) # 기타 레슨 데이터 저장 리스트
start = 0
end = 0

for i in A:
    if start < i: # A 리스트 중 최댓값
        start = i
    end += i # A 리스트의 총합

while start <= end:
    middle = int((start + end) / 2)
    sum = 0 # 레슨 합
    count = 0 # 현재 사용한 블루레이 개수
    for i in range(N):
        if sum + A[i] > middle: # 레슨합 + 현재 레슨 시간 > 중간 인덱스
            count += 1 # 현재 블루레이에 저장할 수 없어 새로운 블루레이로 교체
            sum = 0
        sum += A[i]
    if sum != 0: # sum이 0이 아니면 마지막 블루레이가 필요하므로 count값 올리기
        count += 1
    if count > M: # 중간 인덱스값으로 모든 레슨 저장 불가능
        start = middle + 1
    else: # 중간 인덱스값으로 모든 레슨 저장 가능
        end = middle - 1
print(start)

# 배열에서 K번째 수 찾기
N = int(input()) # 리스트의 크기
K = int(input()) # 구하고자 하는 index
start = 1 # 시작 인덱스
end = K # 종료 인덱스
ans = 0 # 정답

while start <= end: # 이진 탐색 수행
    middle = int((start + end) / 2) # 중앙 인덱스
    cnt = 0 # 중앙값보다 작은 수
    # 중앙값보다 작은 수 계산
    for i in range(1, N + 1):
        cnt += min(int(middle / i), N)
    if cnt < K: # 현재 중앙값보다 작은 수의 개수가 K보다 작음
        start = middle + 1
    else: # 현재 중앙값보다 작은 수의 개수가 K보다 크거나 같음
        ans = middle
        end = middle - 1

print(ans)