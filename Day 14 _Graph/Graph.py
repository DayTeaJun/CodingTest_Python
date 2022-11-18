# 특정 거리의 도시 찾기
from collections import deque

N, M, K, X = map(int, input().split()) # 노드의 수, 에지의 수, 목표 거리, 시작점
A = [[] for _ in range(N + 1)] # 그래프 데이터 저장 인접 리스트
answer = []
visited = [-1] * (N + 1) # 방문 거리 저장 리스트 -1 로 초기화

def BFS(v):
    queue = deque()
    queue.append(v) # 큐 자료구조에 시작 노드 삽입
    visited[v] += 1 # visited 리스트에 현재 노드 방문 기록, 거리 저장 형태로 1 증가
    while queue: # 큐가 비어있을 때까지
        now_Node = queue.popleft() # 큐에서 노드 가져오기
        for i in A[now_Node]:
            if visited[i] == -1: # 현재 노드의 연결 노드 중 미 방문 노드
                visited[i] = visited[now_Node] + 1 # visited 리스트값 1 증가
                queue.append(i) # 큐에 노드 삽입

for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)
    
BFS(X)

for i in range(N + 1):
    if visited[i] == K: # 방문 거리가 K인 노드의 숫자를 정답리스트에 더하기
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i) # 리스트 오름차순 정렬 출력

# 효율적으로 해킹하기
from collections import deque
N, M = map(int, input().split()) # N 노드 개수, M 에지 개수
A = [[] for _ in range(N + 1)] # 그래프 데이터 저장 인접 리스트
answer = [0] * (N + 1)

def BFS(v):
    queue = deque()
    queue.append(v) # 큐 자료구조에 시작 노드 삽입
    visited[v] = True
    while queue: # 큐가 비어있을 때까지
        now_Node = queue.popleft() # 큐에서 노드 가져오기
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True # visited 리스트 노드 방문 기록
                answer[i] += 1 # 신규 노드 인덱스의 정답 리스트값을 증가
                queue.append(i) # 큐에 노드 삽입

for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)
    
for i in range(1, N + 1): # 모든 노드에서 BFS 실행
    visited = [False] * (N + 1) # 방문 여부 저장 초기화
    BFS(i)

maxVal = 0
for i in range(1, N + 1):
    maxVal = max(maxVal, answer[i]) # answer 리스트에서 가장 큰 수 찾기
    
for i in range(1, N + 1):
    if maxVal == answer[i]:
        print(i, end=' ') # answer 리스트에서 maxVal와 같은 값을 가진 index를 정답으로 출력
        
# 이분 그래프 판별하기
N = int(input()) # 테스트 케이스 개수
IsEven = True # 이분그래프 판별 변수

def DFS(node):
    global IsEven
    visited[node] = True
    for i in A[node]:
        if not visited[i]:
            # 인접 노드는 같은 집합이 아니므로 다른 집합으로 처리
            check[i] = (check[node]+1)%2
            DFS(i)
        # 이미 방문한 노드가 현재 내 노드와 같은 집합이면 이분 그래프 아님
        elif check[node] == check[i]:
            IsEven = False

for _ in range(N):
    V, E = map(int, input().split()) # V 노드 개수, E 에지 개수
    A = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    check = [0] * (V + 1) # 노드별 집합 저장 리스트
    IsEven = True
    
    for i in range(E):
        Start, End = map(int, input().split()) # A 인접 리스트에 그래프 데이터 저장하기
        A[Start].append(End)
        A[End].append(Start)
        
    # 주어진 그래프가 항상 1개가 아니므로 모든 노드에서 수행
    for i in range(1, V + 1):
        if IsEven:
            DFS(i)
        else:
            break
        
    if IsEven:
        print("YES")
    else:
        print("NO")

# 물의 양 구하기
from collections import deque

# 두 리스트를 이용하여 6가지 이동 케이스를 간편하게 정의할 수 있다.
# 여기에서 0, 1, 2는 각각 A, B, C 물통을 뜻한다.
# 예시 :index = 0의 경우 Sender[0] : 0, Receiver[0] : 1이기 때문에 A -> B 케이스를 뜻한다.
Sender = [0, 0, 1, 1, 2, 2]
Receiver = [1, 2, 0, 2, 0, 1]
now = list(map(int, input().split())) # A, B, C 값 저장
visited = [[False for j in range(201)] for i in range(201)] # 방문 여부 저장 리스트
answer = [False] * 201 # 정답 리스트

def BFS():
    queue = deque()
    queue.append((0, 0)) # A와 B가 0인 상태로 0, 0 노드에서 시작하기
    visited[0][0] = True
    while queue:
        now_Node = queue.popleft()
        A = now_Node[0]
        B = now_Node[1]
        C = now[2] - A - B # C는 전체 물의 양에서 A와 B를 뺀 것
        for k in range(6): # A -> B, A -> C, B -> A, C -> A, C -> B 케이스 반복
            next = [A, B, C]
            next[Receiver[k]] += next[Sender[k]] # 받는 물통에 보내려는 물통의 값을 더하기
            next[Sender[k]] = 0 # 보내려는 물통의 값을 0으로 업데이트 하기
            if next[Receiver[k]] > now[Receiver[k]]: # 물이 넘칠 때
                next[Sender[k]] = next[Receiver[k]] - now[Receiver[k]] # 초과하는 만큼 다시 이전 물통에 넣어 주기
                next[Receiver[k]] = now[Receiver[k]] # 대상 물통 최대로 채우기
            if not visited[next[0]][next[1]]: # A와 B의 물의 양으로 방문 리스트 체크
                visited[next[0]][next[1]] = True
                queue.append((next[0], next[1]))
                if next[0] == 0: # A의 물의 양이 0일 때 C의 물의 무게를 정답 변수에 저장
                    answer[next[2]] = True

BFS()

for i in range(len(answer)):
    if answer[i]:
        print(i, end=' ') # answer 리스트에서 값이 True인 index를 정답으로 출력