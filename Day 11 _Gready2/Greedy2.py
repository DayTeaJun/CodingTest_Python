# 회의실 배정하기
N = int(input()) # 회의 개수
A = [[0] * 2 for _ in range(N)] # A 회의 정보 저장

# 종료 시각 기준으로 정렬, 종료 시각이 같으면 시작 시각 기준 정렬
for i in range(N):
    S, E = map(int, input().split())
    A[i][0] = E
    A[i][1] = S
    
A.sort()
count = 0
end = -1

for i in range(N):
    if A[i][1] >= end: # 앞 회의 종료 시각보다 시작 시각이 늦은 회의가 나온 경우
        end = A[i][0] # 현재 회의의 종료 시각으로 종료 시각 업데이트
        count += 1 # 진행할 수 있는 회의수 1 증가

print(count) # 총 진행 가능 회의 수 출력

# 최솟값을 만드는 괄호 배치 찾기
answer = 0 # 정답 변수
A = list(map(str, input().split("-"))) # 들어온 데이터를 "-" 기호를 기준으로 split

def mySun(i): # -로 나뉜 그룹들의 합을 구하는 함수
    sum = 0
    temp = str(i).split("+") # "+" 기호를 기준으로 split
    for i in temp:
        sum += int(i) # string값을 int 값으로 변환해 리턴값에 더하기
    return sum

for i in range(len(A)):
    temp = mySun(A[i])
    if i == 0:
        answer += temp
    else:
        answer -= temp
        
print(answer)