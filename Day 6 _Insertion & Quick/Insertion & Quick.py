# ATM 인출 시간 계산하기
N = int(input()) # 사람 수
A = list(map(int, input().split())) # 자릿수별로 구분해 저장한 리스트
S = [0]*N # A 합 배열: 각 사람이 인출을 완료하는 데 필요한 시간을 저장

for i in range(1, N):
    insert_point = i
    insert_value = A[i]
    for j in range(i-1, -1, -1): # 현재 범위에서 삽입 위치 찾기
        if A[j] < A[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1): # 삽입을 위해 삽입 위치에서 i까지 데이터를 한 칸씩 뒤로 밀기
        A[j] = A[j-1]
    A[insert_point] = insert_value # 삽입 위치에 현재 데이터 저장
    
S[0] = A[0]

for i in range(1, N):
    S[i] = S[i-1] + A[i] # A 리스트를 통한 합 배열 S 만들기
    
sum = 0

for i in range(0, N):
    sum += S[i] # S 리스트의 각 데이터값을 모두 합해 결과 출력

print(sum)

# K번째 수 구하기
N, K = map(int, input().split()) # N 숫자의 개수 K K번째 수
A = list(map(int, input().split()))

def quickSort(S, E, K): # 퀵 정렬 함수 S 시작, E 종료, K K번째 수
    global A
    if S < E:
        pivot = partition(S, E)
        if pivot == K: # K번째 수가 pivot이면 더는 구할 필요 없음
            return
        elif K < pivot: # K가 pivot보다 작으면 왼쪽 그룹만 정렬
            quickSort(S, pivot - 1, K)
        else: # K가 pivot보다 크면 오른쪽 그룹만 정렬
            quickSort(pivot + 1, E, K)

def swap(i, j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    
def partition(S, E): # 피벗 구하기 함수
    global A
    
    if S + 1 == E:
        if A[S] > A[E]:
            swap(S, E)
        return

    M = (S + E) // 2 # M 중앙값
    swap(S, M) # 중앙값과 시작 위치와 swap
    pivot = A[S] # 피벗을 시작 위치 값 A[S]로 저장
    i = S + 1 # 시작점
    j = E # 종료점
    
    while i <= j:
        while pivot < A[j] and j > 0: # 피벗보다 큰 수가 나올 때까지 i 증가
            j = j - 1
        while pivot > A[i] and i < len(A)-1: # 피벗보다 작은 수가 나올 때까지 j 감소
            i = i + 1
        if i <= j:
            swap(i, j) # 찾은 i와 j 데이터를 swap
            i = i + 1
            j = j - 1
    # i == j 피벗의 값을 양쪽으로 분리한 가운데에 오도록 설정하기
    A[S] = A[j]
    A[j] = pivot
    return j

quickSort(0, N - 1, K - 1) # 퀵 정렬 실행
print(A[K - 1])