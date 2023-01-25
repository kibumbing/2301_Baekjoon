from collections import deque
from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

mutal = [9, 3, 1]
permut = list(permutations(mutal, n))

deq = deque([])
deq.append([arr, 0])
visited = list(set())
visited.append(arr)
count = 0
while deq:
    scv, count = deq.popleft()
    done = 0
    for i in range(n):
        if scv[i] <= 0:
            done += 1
    if done == n:
        print(count)
        exit()
    for i in range(len(permut)):
        scv_hurt = []
        for j in range(n):
            scv_hurt.append(scv[j] - permut[i][j])
        if scv_hurt not in visited:
            deq.append([scv_hurt, count+1])
            visited.append(scv_hurt)