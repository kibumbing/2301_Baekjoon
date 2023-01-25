from collections import deque

n, m = map(int, input().split())
arr = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
for i in range(n):
    temp = input()
    for j in range(m):
        if temp[j] == '1':
            arr[i][j][0] = -1
            arr[i][j][1] = -1
if n == 1 and m == 1:
    print(1)
    exit()

arr[0][0][0] = 1
arr[0][0][1] = 1

deq = deque()
deq.append([0, 0, 0])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while deq:
    x, y, z = deq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx == n - 1 and ny == m - 1:
            if z == 1:
                print(arr[x][y][1] + 1)
                exit()
            else:
                print(arr[x][y][0] + 1)
                exit()
        if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
            continue

        if z == 0 and arr[nx][ny][0] == 0:
            arr[nx][ny][0] = arr[x][y][0] + 1
            deq.append([nx, ny, 0])
        elif z == 0 and arr[nx][ny][1] == -1:
            arr[nx][ny][1] = arr[x][y][0] + 1
            deq.append([nx, ny, 1])
        elif z == 1 and arr[nx][ny][1] == 0:
            arr[nx][ny][1] = arr[x][y][1] + 1
            deq.append([nx, ny, 1])
print(-1)


