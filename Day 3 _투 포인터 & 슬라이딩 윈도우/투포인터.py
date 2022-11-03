# 연속된 자연수의 합 구하기
# 자연수 N은 몇 개의 연속된 자연수의 합으로 나타낼 수 있다. 자연수 N(1 <= N <= 10,000,000)을 몇 개의 연속된 자연수의 합으로 나타내는 가짓수 출력하는 문제
n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1 # 변수 초기화

while end_index != n:
    if sum == n: # 정답 케이스
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)

# 주몽의 명령
# 1번 째 줄에 재료의 개수 N(1 <= N <= 15,000), 2번째 줄에 갑옷을 만드는 데 필요한 수 M(1 <= M <= 10,000,000)이 주어진다.
# 3번째 줄에는 N개의 재료들이 가진 고유한 번호들이 공백을 사이에 두고 주어진다. 고유한 번호는 100,00보다 작거나 같은 자연수다.
import sys
input = sys.stdin.readline
N = int(input()) # 재료의 개수
M = int(input()) # 갑옷이 되는 번호
A = list(map(int, input().split())) # 재료 데이터 저장 리스트
A.sort() # 리스트 정렬하기
count = 0 # 정답 값
i = 0 # 시작 인덱스
j = N - 1 # 종료 인덱스

while i < j:
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1
        
print(count)

# 좋은 수 구하기
# 1번째 줄에 수의 개수 N(1 <= N <= 2,000), 2번째 줄에 N개의 수의 값(Ai)이 주어진다 (|Ai| <= 1,000,000,000, Ai는 정수).
import sys
input = sys.stdin.readline
N = int(input()) # 데이터의 수
Result = 0 # 좋은 수 개수 저장 변수
A = list(map(int, input().split())) # 수 데이터 저장 리스트
A.sort() # 리스트 정렬

for k in range(N):
    find = A[k] # 변수 초기화 = 찾고자 하는 값 find = A[k]
    i = 0 # 포인터
    j = N - 1 # 포인터
    while i < j: # 투 포인터 알고리즘
        if A[i] + A[j] == find: # find는 서로 다른 두 수의 합이어야 함을 체크
            if i != k and j !=k: # 두 포인터가 k가 아닐 때 좋은 수 개수 1 증가 및 while문 종료
                Result += 1
                break
            elif i == k: # 포인터가 k가 맞을 때 포인터 변경 및 계속 주행
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1
            
print(Result)