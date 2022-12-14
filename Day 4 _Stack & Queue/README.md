# 스택
스택은 삽입과 삭제 연산이 후입선출(Last-In First-Out)로 이루어지는 자료구조</br>
후입선출은 삭제가 한쪽에서만 일어나는 특징이 있다.  

위치  
top : 삽입과 삭제가 일어나는 위치 (맨위)

연산  
s.append(data) : top 위치에 새로운 데이터를 삽입하는 연산  
s.pop() : top 위치에 현재 있는 데이터를 삭제하고 확인하는 연산  
s(-1) : top 위치에 현재 있는 데이터를 단순 확인하는 연산  

스택은 깊이 우선 탐색(DFS), 백트래킹 종류의 코딩 테스트에 효과적  
스택은 재귀 함수 알고리즘의 원리와 비슷함.

# 큐
큐는 삽입과 삭제 연산이 선입선출(First-In First-Out)로 이루어지는 자료구조  
선입선출은 삭제가 양방향으로 일어나는 특징이 있다.

위치  
rear : 큐에서 가장 끝 데이터를 가리키는 영역  
front : 큐에서 가장 앞의 데이터를 가리키는 영역  

연산(리스트 이름이 s일 때)  
s.append(data) : rear 부분에 새로운 데이터를 삽입하는 연산  
s.popleft() : front 부분에 있는 데이터를 삭제하고 확인하는 연산  
s[0] : 큐의 맨 앞(front)에 있는 데이터를 확인할 때 사용하는 연산  

큐는 너비 우선 탐색(BFS)에서 자주 사용

* 우선 순위 큐 : 들어간 순서와 상관 없이 우선순위가 높은 데이터가 먼저 나오는 자료구조.  
큐 설정에 따라 front에 항상 최댓값 또는 최솟값이 위치한다.  
힙을 이용해 구현하며 힙은 트리 종류 중 하나이다.

# 스택으로 수열 만들기 백준 1874번
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

입력  
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

출력  
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

# 오큰수 구하기 백준 17298번
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

입력  
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

출력  
총 N개의 수 NGE(1), NGE(2), ..., NGE(N)을 공백으로 구분해 출력한다.

# 카드게임 백준 2164번
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

입력  
첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.

출력  
첫째 줄에 남게 되는 카드의 번호를 출력한다

# 절댓값 힙 구현하기 백준 11286번
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

배열에 정수 x (x ≠ 0)를 넣는다.  
배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.  
프로그램은 처음에 비어있는 배열에서 시작하게 된다.  

입력  
첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 정수는 -231보다 크고, 231보다 작다.

출력  
입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.
