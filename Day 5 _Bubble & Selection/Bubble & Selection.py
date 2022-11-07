# 수 정렬하기 1 
N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]: # 현재 A 리스트의 값보다 1칸 오른쪽 리스트의 값이 더 작으면 두 수 바꾸기
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
            
for i in range(N):
    print(A[i])


# 버블 정렬 프로그램 1
N = int(input())
A = []

for i in range(N):
    A.append((int(input()), i))
    
Max = 0
sorted_A = sorted(A) # A 리스트 정렬

for i in range(N):
    if Max < sorted_A[i][1] - i:
        Max = sorted_A[i][1] - i # A[i]의 정렬 전 index - 정렬 후 index 계산의 최댓값을 찾아 저장

print(Max + 1) # 최댓값 + 1 정답


# 내림차순으로 자릿수 정렬하기
A = list(input())

for i in range(len(A)):
    Max = i
    for j in range(i+1, len(A)):
        if A[j] > A[Max]: # 내림차순으로 최댓값을 찾음
            Max = j
            
    if A[i] < A[Max]: # 현재 i의 값과 Max값 중 Max값이 더 크면 swap을 수행
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp
        
for i in range(len(A)):
    print(A[i])