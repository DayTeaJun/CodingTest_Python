# 수 정렬하기 2
import sys

input = sys.stdin.readline
print = sys.stdout.write
    
def merge_sort(s, e): # 병합 정렬 수행
    if e - s < 1: # s 시작점 e 종료점 m 중간점
        return
    m = int(s + (e - s) / 2)
    merge_sort(s, m)
    merge_sort(m + 1, e)
    for i in range(s, e + 1):
        tmp[i] = A[i] # tmp 리스트 저장
    k = s
    index1 = s # 앞 그룹 시작점
    index2 = m + 1 # 뒷 그룹 시작점
    while index1 <= m and index2 <= e: # index1 중간점 index2 종료점
        if tmp[index1] > tmp[index2]: # 더 작은 수를 선택해 리스트에 저장
            A[k] = tmp[index2]
            k += 1 # 선택된 데이터의 index값을 오른쪽으로 한칸 이동
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input()) # 정렬할 개수
A = [0] * int(N + 1) # 정렬할 리스트 선언
tmp = [0] * int(N + 1) # 정렬할 때 잠시 사용할 임시 리스트 선언

for i in range(1, N + 1):
    A[i] = int(input())
    
merge_sort(1, N)

for i in range(1, N + 1):
    print(str(A[i]) + '\n')

# 버블 정렬 프로그램 2
result = 0

def merge_sort(s, e): # 병렬 정렬
    global result
    if e - s < 1:
        return
    m = int(s + (e - s) / 2)
    merge_sort(s, m) # 재귀 함수 형태 구현
    merge_sort(m + 1, e)
    for i in range(s, e + 1):
        tmp[i] = A[i]
    k = s
    index1 = s # 앞쪽 그룹 시작점
    index2 = m + 1 # 뒤쪽 그룹 시작점
    while index1 <= m and index2 <= e: # 두 그룹을 병합하는 로직
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k # 뒤쪽 데이터값이 더 작다면 결괏값 업데이트
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N= int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
tmp = [0] * int(N + 1)
merge_sort(1, N)
print(result)

# 수 정렬하기 3
N = int(input())
count = [0] * 10001 # 카운트 정렬 리스트

for i in range(N):
    count[int(input())] += 1 # count 리스트에 현재 수에 해당하는 index의 값 1 증가

for i in range(10001):
    if count[i] != 0: # i가 기존 input에 있는 수
        for _ in range(count[i]): # 해당 index값만큼 index를 반복하여 출력
            print(i)