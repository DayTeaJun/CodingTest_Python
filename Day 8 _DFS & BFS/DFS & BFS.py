# 연결 요소의 개수 구하기
# n, m = map(int, input().split()) # n 노드 개수 m 에지 개수
# A = [[] for _ in range(n+1)] # 그래프 데이터 저장 인접 리스트 초기화
# visited = [False] * (n+1) # 방문 기록 리스트 초기화

# def DFS(v):
#     visited[v] = True # visited 리스트에 현재 노드 방문 기록
#     for i in A[v]:
#         if not visited[i]: # 현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행(재귀 함수 형태)
#             DFS(i)

# for _ in range(m):
#     s, e = map(int, input().split())  # A 인접 리스트에 그래프 데이터 저장
#     A[s].append(e)
#     A[e].append(s)
    
# count = 0

# for i in range(1, n+1):
#     if not visited[i]:
#         count += 1
#         DFS(i)

# print(count)

# 신기한 소수 찾기
# N = int(input()) # 자릿수

# def isPrime(num): # 소수 구하기 함수
#     for i in range(2, int(num / 2 + 1)):
#         if num % i == 0:
#             return False # 소수가 아닌 경우
#     return True

# def DFS(number):
#     if len(str(number)) == N:
#         print(number)
#     else:
#         for i in range(1, 10):
#             if i % 2 == 0: # 짝수라면 더는 탐색 불필요
#                 continue
#             if isPrime(number * 10 + i): # 소수이면 자릿수 늘림
#                 DFS(number * 10 + i)

# # 일의 자리 소수는 2, 3, 5, 7 이므로 4가지 수 에서만 시작
# DFS(2)
# DFS(3)
# DFS(5)
# DFS(7)

# 친구 관계 파악하기
# N, M = map(int, input().split())
# arrive = False # 도착 확인 변수
# A = [[] for _ in range(N + 1)]
# visited = [False] * (N + 1) # 방문 기록 저장 리스트

# def DFS(now, depth):
#     global arrive
#     if depth == 5: # 깊이가 5가 되면 종료
#         arrive = True
#         return
#     visited[now] = True
    
#     for i in A[now]: # 현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행
#         if not visited[i]:
#             DFS(i, depth + 1) # 재귀 호출마다 깊이 증가
#     visited[now] = False
    
# for _ in range(M):
#     s, e = map(int, input().split())
#     A[s].append(e) # 양방향 에지이므로 양쪽에 에지 더하기
#     A[e].append(s)

# for i in range(N):
#     DFS(i, 1)
#     if arrive:
#         break # depth가 5에 도달한 적이 있다면 종료
# if arrive:
#     print(1)
# else:
#     print(0)

# DFS와 BFS 프로그램
# from collections import deque
# N, M, Start = map(int, input().split())
# A = [[] for _ in range(N + 1)]

# for _ in range(M):
#     s, e = map(int, input().split())
#     A[s].append(e)
#     A[e].append(s)

# for i in range(N + 1):
#     A[i].sort()

# # DFS 구현하기
# def DFS(v):
#     print(v, end=' ') # 현재 노드 출력하기
#     visited[v] = True # visited 리스트에 현재 노드 방문 기록하기
#     for i in A[v]: 
#         if not visited[i]:
#             DFS(i) # 현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행하기(재귀 함수 형태)

# visited = [False] * (N + 1)
# DFS(Start)

# # BFS 구현하기
# def BFS(v):
#     queue = deque()
#     queue.append(v)
#     visited[v] = True
#     while queue:
#         now_Node = queue.popleft() # 큐에서 노드 데이터를 가져오기
#         print(now_Node, end=' ') # 가져온 노드 출력
#         for i in A[now_Node]: # 가져온 노드 출력
#             if not visited[i]: # 현재 노드의 연결 노드 중 미 방문 노드를 큐에 삽입하고 방문 리스트에 기록
#                 visited[i] = True
#                 queue.append(i)

# print()
# visited = [False] * (N + 1)
# BFS(Start)

# 미로 탐색하기
# from collections import deque
# dx = [0, 1, 0, -1] # 상하좌우를 탐색하기 위한 리스트 선언
# dy = [1, 0, -1, 0]
# N, M = map(int, input().split())
# A = [[0] * M for _ in range(N)]
# visited = [[False] * M for _ in range(N)]

# for i in range(N):
#     numbers = list(input())
#     for j in range(M):
#         A[i][j] = int(numbers[j])

# def BFS(i, j):
#     queue = deque()
#     queue.append((i, j))
#     visited[i][j] = True
#     while queue:
#         now = queue.popleft() # 큐에서 데이터를 가져오기
#         for k in range(4): # 상하좌우 탐색
#             x = now[0] + dx[k]
#             y = now[1] + dy[k]
#             if x >= 0 and y >= 0 and x < N and y < M: # 유효한 좌표
#                 if A[x][y] != 0 and not visited[x][y]: # 이동할 수 있는 칸이면서 방문하지 않은 노드
#                     visited[x][y] = True
#                     A[x][y] = A[now[0]][now[1]] + 1 # A 리스트에 depth를 현재 노드의 depth + 1로 업데이트
#                     queue.append((x, y))

# BFS(0, 0)
# print(A[N - 1][M - 1])

# 트리의 지름 구하기
from collections import deque

N = int(input())
A = [[] for _ in range(N + 1)]

for _ in range(N):
    Data = list(map(int, input().split()))
    index = 0
    S = Data[index]
    index += 1
    while True:
        E = Data[index]
        if E == -1:
            break
        V = Data[index + 1]
        A[S].append((E, V))
        index += 2
        
distance = [0] * (N + 1)
visited = [False] * (N + 1)

# BFS 구현
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_Node] + i[1] # 큐에 삽입 된 노드 거리 = 현재 노드의 거리 + 에지의 가중치로 변경

BFS(1)
Max = 1

for i in range(2, N + 1):
    if distance[Max] < distance[i]:
        Max = i # 거리 리스트값 중 Max값으로 시작점 재설정
        
distance = [0] * (N + 1)
visited = [False] * (N + 1)
BFS(Max)
distance.sort()
print(distance[N])