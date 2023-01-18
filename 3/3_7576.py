# 시간 복잡도 - O(n*m)

from collections import deque

n, m = map(int, input().split())
arr = [[0]*n for i in range(m)]
count = n * m
queue = deque()
for i in range(m):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            arr[i][j] = 1
            queue.append([i, j])
            count -= 1
        elif temp[j] == -1:
            arr[i][j] = -1
            count -= 1
max = 1
move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]
while queue:
    a, b = queue.popleft()
    tar = arr[a][b]
    for i in range(4):
        if a + move_x[i] > m - 1 or a + move_x[i] < 0:
            continue
        if b + move_y[i] > n - 1 or b + move_y[i] < 0:
            continue
        if arr[a + move_x[i]][b + move_y[i]] == 0:
            count -= 1
            queue.append([a + move_x[i], b + move_y[i]])
            arr[a + move_x[i]][b + move_y[i]] = tar + 1
            if max < tar + 1:
                max = tar + 1

if count == 0:
    print(max-1)
else:
    print(-1)