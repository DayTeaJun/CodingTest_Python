import random
findNumber = random.randrange(1, 101) # 1 ~ 100 사이 랜덤값 생성

for i in range(1, 101):
    if i == findNumber:
        print(i)
        break
"""
위 코드의 시간 복잡도
빅-오메가 -> 값을 운좋게 한번에 찾을 경우 (1번)
빅-세타 -> 평균적으로 값을 찾을 경우 (N/2번)
빅-오 -> 값을 마지막에 찾을 경우 (N번)

코딩테스트에서는 빅-오(최악) 표기법을 기준으로 계산을 하는 것이 좋다.
(다양한 테스트 케이스를 통과해야하기 때문)
"""

"""
버블 정렬 O(n^2) 과 병합 정렬 O(nlogn) 의 시간 복잡도로 문제 풀기

* 1번째 줄에 수의 개수 N(1 <= N <= 1,000,000), 이 수는 절댓값이 1,000,000보다 작거나 같은 정수다. 수는 중복되지 않는다.
"""

n = int(input()) # 입력변수 저장
s = [] # 빈 리스트 생성

for i in range(n):
    s.append(int(input()))
    # 입력받은 변수만큼 리스트에 저장
    
# 버블 정렬 O(n^2)
for i in range(len(s)):
    for j in range(len(s)):
        if s[i] < s[j]:
            s[i], s[j] = s[j], s[i]
for num in s:
    print(num) # 버블 정렬 나열
    
number = int(input())
input_list = []

for _ in range(number):
    input_list.append(int(input()))

# 병합 정렬 O(nlogn)
number = int(input()) # 입력변수 저장
input_list = [] # 빈 리스트 생성

for _ in range(number):
    input_list.append(int(input()))
    # 입력받은 변수만큼 리스트에 저장
    
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left_list = merge_sort(lst[:mid])
    right_list = merge_sort(lst[mid:])
    return merge(left_list,right_list)
    # 병합정렬 반으로 분할

def merge(left_list, right_list):
    sorted_list = []
    li = 0
    ri = 0
    while (li < len(left_list) and ri < len(right_list)):
        if left_list[li] < right_list[ri]:
            sorted_list.append(left_list[li])
            li += 1
        else:
            sorted_list.append(right_list[ri])
            ri += 1

    while(li < len(left_list)):
        sorted_list.append(left_list[li])
        li += 1
    while (ri < len(right_list)):
        sorted_list.append(right_list[ri])
        ri += 1
    return sorted_list
    # 병합정렬 결합
    
input_list = merge_sort(input_list)

for item in input_list:
    print(item) # 병합 정렬 나열
    
"""
시간 제한이 2초이므로 4,000만 번 이하의 연산 횟수로 문제를 해결해야 함. (최악의 경우를 상정)
연산 횟수 = 알고리즘 시간 복잡도 n값에 데이터의 최대 크기를 대입하여 도출

버블 정렬 = (1,000,000)^2 > 4,000만 -> 부적합
병합 정렬 = 1,000,000log2(1,000,000) < 4,000만 -> 적합
데이터의 크기로 알고리즘을 정해야 함.
"""