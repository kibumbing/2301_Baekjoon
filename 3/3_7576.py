# 시간 복잡도 - O(n*m)

from collections import deque

n, m = map(int, input().split())    # 창고 크기 입력
arr = [[0]*n for i in range(m)]     # 창고 입력 배열
count = n * m   # 익지 않은 토마토의 수
queue = deque() # 너비 우선 탐색을 위한 큐
# 토마토 정보 입력
for i in range(m):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:    # 토마토가 익은 경우
            arr[i][j] = 1   # 배열 업데이트
            queue.append([i, j])    # 큐 업데이트
            count -= 1      # 익지 않은 토마토의 수 - 1
        elif temp[j] == -1: # 토마토가 들어 있지 않은 경우
            arr[i][j] = -1  # 배열 업데이트
            count -= 1      # 익지 않은 토마토의 수 - 1
max = 1 # 토마토가 모두 익을 때까지의 최소 날짜
move_x = [-1, 1, 0, 0]  # 검사할 x방향
move_y = [0, 0, -1, 1]  # 검사할 y방향
# 너비 우선 탐색
while queue:
    a, b = queue.popleft()  # 검사할 현재 위치
    tar = arr[a][b]         # 검사할 위치
    for i in range(4):      # 모든 방향 검사
        # 검사할 위치가 배열을 초과할 경우 검사하지 않음
        if a + move_x[i] > m - 1 or a + move_x[i] < 0:
            continue
        if b + move_y[i] > n - 1 or b + move_y[i] < 0:
            continue
        # 검사한 인접 토마토가 익지 않았을 경우
        if arr[a + move_x[i]][b + move_y[i]] == 0:
            count -= 1  # 익지 않은 토마토의 수 - 1
            queue.append([a + move_x[i], b + move_y[i]])    # 큐 업데이트
            arr[a + move_x[i]][b + move_y[i]] = tar + 1     # 익을 때까지의 날짜 업데이트
            if max < tar + 1:   # 최소 날짜 업데이트
                max = tar + 1

# 출력
if count == 0:
    print(max-1)
else:
    print(-1)