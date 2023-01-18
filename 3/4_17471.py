from collections import deque
from itertools import combinations

n = int(input())
man_num = list(map(int, input().split()))
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    temp.pop(0)
    arr.append(temp)

num = [i for i in range(n)]
area = []
for i in range(1, n):
    temp = list(combinations(num, i))
    for j in temp:
        area.append(list(j))

area_2 = []
for i in range(len(area)):
    deq = deque()
    visited = deque()
    deq.append(area[i][0])
    visited.append(area[i][0])
    while deq:
        pop_num = deq.popleft()
        for j in arr[pop_num]:
            if j-1 in area[i] and j-1 not in visited:
                deq.append(j-1)
                visited.append(j-1)
    if sorted(area[i]) == sorted(visited):
        area_2.append(area[i])

area_3 = []
area_4 = []
for i in range(len(area_2)):
    temp = num.copy()
    for j in area_2[i]:
        temp.remove(j)
    if temp in area_2:
        area_3.append(area_2[i])
        area_4.append(temp)

min = int(1e9)
for i in range(len(area_3)//2):
    sum1 = 0
    for j in area_3[i]:
        sum1 += man_num[j]
    sum2 = 0
    for k in area_4[i]:
        sum2 += man_num[k]
    if abs(sum1-sum2) < min:
        min = abs(sum1-sum2)

if min != int(1e9):
    print(min)
else:
    print(-1)
