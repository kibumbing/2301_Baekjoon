# 시간 복잡도 - O(n*m)

n, m = map(int, input().split())
arr = [[0]*m for i in range(n)]
for i in range(n):
    str = input()
    for j in range(len(str)):
        arr[i][j] = int(str[j])

count = [[int(1e9)]*m for i in range(n)]
count[0][0] = 1
queue = [[0, 0]]
while len(queue):
    a, b = queue.pop(0)
    tar = count[a][b]
    move_x = [-1, 1, 0, 0]
    move_y = [0, 0, -1, 1]
    for i in range(4):
        if a + move_x[i] > n - 1 or a + move_x[i] < 0:
            continue
        if b + move_y[i] > m - 1 or b + move_y[i] < 0:
            continue
        if arr[a + move_x[i]][b + move_y[i]] == 1 and count[a + move_x[i]][b + move_y[i]] > tar + 1:
            queue.append([a + move_x[i], b + move_y[i]])
            count[a + move_x[i]][b + move_y[i]] = tar + 1

print(count[n-1][m-1])