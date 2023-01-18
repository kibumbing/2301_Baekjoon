# 시간 복잡도 - O(n^2)

# 입력
n = int(input())
arr = [[0]*(n+2) for i in range(n+2)]
for i in range(1, n+1):
    str = input()
    for j in range(len(str)):
        if str[j] == '1':
            arr[i][j+1] = -1

count = 0
home_count = []
for i in range(1, n+2):
    for j in range(1, n+2):
        if arr[i][j] == -1:
            count += 1
            queue = [[i,j]]
            visited = [[i,j]]
            while len(queue):
                a, b = queue.pop(0)
                arr[a][b] = count
                if arr[a-1][b] == -1 and [a-1, b] not in visited:
                    queue.append([a - 1, b])
                    visited.append([a - 1, b])
                if arr[a][b - 1] == -1 and [a, b - 1] not in visited:
                    queue.append([a, b - 1])
                    visited.append([a, b - 1])
                if arr[a+1][b] == -1 and [a+1, b] not in visited:
                    queue.append([a + 1, b])
                    visited.append([a + 1, b])
                if arr[a][b+1] == -1 and [a, b+1] not in visited:
                    queue.append([a, b + 1])
                    visited.append([a, b + 1])
            home_count.append(len(visited))

print(count)
home_count.sort()
for i in range(count):
    print(home_count[i])