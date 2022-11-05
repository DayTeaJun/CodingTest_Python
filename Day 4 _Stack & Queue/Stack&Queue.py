# 스택으로 수열 만들기
N = int(input()) # 수열 개수
A = [0]*N # 수열 리스트 채우기

for i in range(N): # 수열 리스트 채우기
    A[i] = int(input())
    
stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = A[i]
    
    if su >= num: # 현재 수열값 >= 오름차순 자연수: 값이 같아질 때까지 append() 수행
        while su >= num:
            stack.append(num)
            num += 1 # 오름차순 자연수 1 증가
            answer += "+\n" # + 저장
        stack.pop()
        answer += "-\n" # - 저장
    else: # 현재 수열값 < 오름차순 자연수: pop()을 수행 해 수열 원소를 꺼냄
        N = stack.pop()
        # 스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면 수열을 출력할 수 없음
        if N > su:
            print("NO")
            result = False
            break
        else:
            answer += "-\n" # - 저장
            
if result: # NO가 없으면 저장한 값 출력
    print(answer)
    
# 오큰수 구하기
n = int(input()) # 수열 개수
ans = [0] * n # 정답 리스트
A = list(map(int, input().split())) # 수열 리스트
myStack = [] # 스택 선언

for i in range(n):
    # 스택이 비어 있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우
    while myStack and A[myStack[-1] < A[i]]:
        ans[myStack.pop()] = A[i] # 스택에서 pop한 값을 index로 하는 정답 리스트 부분을 수열 리스트의 현재 값(A[i])으로 저장
    myStack.append(i) # 스택에 i 값을 저장
    
while myStack: # 스택이 빌 때까지
    ans[myStack.pop()] = -1 # 스택에 있는 index의 정답 리스트에 -1 저장

result = ""

for i in range(n):
    result += str(ans[i])+ " "

print(result) # 정답 리스트 출력

# 카드 게임
from collections import deque
N = int(input()) # N 카드의 개수
myQueue = deque() # 카드 저장 자료구조

for i in range(1, N+1): # 카드의 개수만큼 반복
    myQueue.append(i) # 큐에 카드 저장
    
while len(myQueue) > 1: # 카드가 1장 남을 때까지
    myQueue.popleft() # 맨 위의 카드를 버림
    myQueue.append(myQueue.popleft()) # 맨 위의 카드를 가장 아래의 카드 밑으로 이동

print(myQueue[0]) # 마지막으로 남은 카드 출력

# 절댓값 힙 구현하기
from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline
N = int(input()) # 질의 요청 개수
myQueue = PriorityQueue() # 우선순위 큐 선언

for i in range(N):
    request = int(input())
    if request == 0: # 요청이 0일 때 큐가 비어 있으면 0, 비어 있지 않으면 큐의 front값 출력(get())
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1]))+'\n')
    else: # 요청이 1일 때, 새로운 데이터를 우선순위 큐에 더하기(put())
        # 절댓값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성
         myQueue.put((abs(request), request))