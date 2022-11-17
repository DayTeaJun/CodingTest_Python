# 최소 공배수 구하기
def gcd(a, b): # 최대 공약수 함수
    if b == 0:
        return a # a가 최대 공약수
    else:
        return gcd(b, a % b) # 재귀 형태로 구현 , a 큰 수 b 작은 수
    
t = int(input()) # 테스트 케이스

for i in range(t):
    a, b = map(int, input().split()) # a 1번째 수, b 2번째 수
    result = a * b / gcd(a, b) # 결괏값 출력
    print(int(result))

# 최대 공약수 구하기
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
a, b = map(int, input().split())
result = gcd(a, b)

while result > 0: # result값만큼 반복하여 1출력
    print(1, end='')
    result -= 1

# 칵테일 만들기
N = int(input()) # 재료의 개수
A = [[] for _ in range(N)] # 인접 리스트
visited = [False] * (N) # DFS(깊이우선탐색)를 탐색할 때 탐색 여부 저장 리스트
D = [0] * (N) # 각 노드값 저장 리스트
lcm = 1 # 최소 공배수

def gcd(a, b): # 최대 공약수 함수 구현
    if b == 0:
        return a
    else:
        return gcd(b, a % b) # 재귀 함수 형태로 구현

def DFS(v): # DFS 탐색 함수 구현
    visited[v] = True
    for i in A[v]:
        next = i[0]
        if not visited[next]: # 현재 노드의 연결 노드 중 방문하지 않은 노드
            D[next] = D[v] * i[2] // i[1] # 다음 노드의 값 = 현재 노드의 값 * 비율로 저장
            DFS(next) # 재귀 형태

for i in range(N - 1):
    a, b, p, q = map(int, input().split())
    A[a].append((b, p, q))
    A[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q)) # 최소 공배수는 두 수의 곱을 최대 공약수로 나눈 것

D[0] = lcm # 0번 노드에 최소 공배수 저장
DFS(0)
mgcd = D[0]

for i in range(1, N): # DFS로 최대 공약수 계산
    mgcd = gcd(mgcd, D[i])

for i in range(N): # D 리스트의 각 값을 최대 공약수로 나눠 정답 출력
    print(int(D[i] // mgcd), end= ' ')

Ax + By = C
a, b, c = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def Execute(a, b): # 유클리드 호제법 함수 구현
    ret = [0] * 2
    if b == 0: # 재귀 함수를 중단하고 x, y를 각각 1, 0으로 설정하여 return
        ret[0] = 1
        ret[1] = 0
        return ret
    q = a // b
    v = Execute(b, a % b)
    ret[0] = v[1]
    ret[1] = v[0] - v[1] * q # 몫을 계산하는 역산 로직 구현, 재귀에서 빠져나오는 영역에서 실행하면 자연스럽게 역순이 됨
    return ret

mgcd = gcd(a, b) # 최대 공약수

if c % mgcd != 0: # 최대 공약수의 배수가 아니면 -1 출력
    print(-1)
else:
    mok = int(c / mgcd)
    ret = Execute(a, b)
    print(ret[0] * mok, end= ' ')
    print(ret[1] * mok)