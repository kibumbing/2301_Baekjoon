from collections import deque

n = int(input())
arr = [[0]*n for i in range(n)]
arr2 = [[0]*n for i in range(n)]
for i in range(n):
    str = input()
    for j in range(len(str)):
        if str[j] == 'R':
            arr[i][j] = 0
            arr2[i][j] = 0
        if str[j] == 'G':
            arr[i][j] = 1
            arr2[i][j] = 0
        if str[j] == 'B':
            arr[i][j] = 2
            arr2[i][j] = 2

check = [[0]*n for i in range(n)]
check2 = [[0]*n for i in range(n)]
count = 0
count2 = 0
for i in range(n):
    for j in range(n):
        deq = deque()
        if check[i][j] != -1:
            count += 1
            deq.append([i, j])
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            while deq:
                a, b = deq.popleft()
                check[a][b] = -1
                temp = arr[a][b]
                for k in range(4):
                    nx = a + dx[k]
                    ny = b + dy[k]
                    if nx > n-1 or nx < 0 or ny > n-1 or ny < 0:
                        continue
                    if arr[nx][ny] == temp and check[nx][ny] == 0:
                        deq.append([nx, ny])
                        check[nx][ny] = -1
        deq = deque()
        if check2[i][j] != -1:
            count2 += 1
            deq.append([i, j])
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            while deq:
                a, b = deq.popleft()
                check2[a][b] = -1
                temp = arr2[a][b]
                for k in range(4):
                    nx = a + dx[k]
                    ny = b + dy[k]
                    if nx > n - 1 or nx < 0 or ny > n - 1 or ny < 0:
                        continue
                    if arr2[nx][ny] == temp and check2[nx][ny] == 0:
                        deq.append([nx, ny])
                        check2[nx][ny] = -1

print(count)
print(count2)