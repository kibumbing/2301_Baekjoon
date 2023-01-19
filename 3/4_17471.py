# 시간 복잡도 - O(n+m)

from collections import deque
from itertools import combinations

n = int(input())    # 구역 개수 입력
man_num = list(map(int, input().split()))   # 구역의 인구 입력
# 각 구역과 인접한 구역의 정보 입력
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    temp.pop(0)
    arr.append(temp)

num = [i for i in range(n)] # 모든 구역의 번호 배열
area = []   # 한 선거구에 들어갈 수 있는 구역의 집합 후보
# 1~(n-1)개의 조합 생성
for i in range(1, n):
    temp = list(combinations(num, i))
    for j in temp:
        area.append(list(j))

# 집합의 모든 원소가 인접되어 있는지 확인 - 너비 우선 탐색
area_2 = []
for i in range(len(area)):  # 모든 집합 확인
    deq = deque()   # 너비 우선 탐색을 위한 큐
    visited = deque()   # 너비 우선 탐색을 통해 탐색한 원소 집합
    deq.append(area[i][0])
    visited.append(area[i][0])
    while deq:
        pop_num = deq.popleft() # 검사할 원소
        for j in arr[pop_num]:  # 검사할 원소에 인접한 원소
            if j-1 in area[i] and j-1 not in visited:   # 집합에 원소가 존재하고, 방문하지 않을 경우
                deq.append(j-1)     # 큐 업데이트
                visited.append(j-1) # 탐색한 원소 업데이트
    if sorted(area[i]) == sorted(visited):  # 너비 우선 탐색으로 전부 탐색이 가능한 경우
        area_2.append(area[i])              # 인접 확인

area_3 = [] # 1번 선거구
area_4 = [] # 2번 선거구
for i in range(len(area_2)):
    temp = num.copy()   # 나머지 구역, 반대 선거구
    for j in area_2[i]:
        temp.remove(j)
    if temp in area_2:  # 반대 선거구도 너비 우선 탐색으로 전부 탐색이 가능한 경우
        area_3.append(area_2[i])    # 1번 선거구 업데이트
        area_4.append(temp)         # 2번 선거구 업데이트

min = int(1e9)  # 최소 차이 저장 변수
for i in range(len(area_3)//2): # 원소가 겹치므로 반만 검사
    # 1번 선거구의 구역 인구 합
    sum1 = 0
    for j in area_3[i]:
        sum1 += man_num[j]
    # 2번 선거구의 구역 인구 합
    sum2 = 0
    for k in area_4[i]:
        sum2 += man_num[k]
    # 차이가 최소값보다 작으면 업데이트
    if abs(sum1-sum2) < min:
        min = abs(sum1-sum2)

# 출력
if min != int(1e9):
    print(min)
else:
    print(-1)
