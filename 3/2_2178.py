# 시간 복잡도 - O(n*m)

n, m = map(int, input().split())    # 미로 크기 입력
# 미로 입력 및 저장
arr = [[0]*m for i in range(n)]
for i in range(n):
    str = input()
    for j in range(len(str)):
        arr[i][j] = int(str[j])

count = [[int(1e9)]*m for i in range(n)]    # 미로 크기의 배열 생성
count[0][0] = 1     # 시작 위치 원소를 1로 초기화(최소 1칸을 지나야 함)
queue = [[0, 0]]    # 너비 우선 탐색을 위한 큐
# 너비 우선 탐색 실행
while len(queue):
    a, b = queue.pop(0)     # 검사할 원소
    tar = count[a][b]       # 검사할 원소의 값(해당 위치에 도달하기 위해 지나야 하는 칸 수)
    move_x = [-1, 1, 0, 0]  # 검사할 x방향
    move_y = [0, 0, -1, 1]  # 검사할 y방향
    for i in range(4):  # 동서남북 검사
        if a + move_x[i] > n - 1 or a + move_x[i] < 0:
            continue
        if b + move_y[i] > m - 1 or b + move_y[i] < 0:
            continue
        # 검사할 칸이 이동 가능하고, 해당 칸에 도달하기 위해 지나햐 하는 칸 수가 현재 위치에 1 더한 값보다 클 경우(최소값을 구해야 함)
        if arr[a + move_x[i]][b + move_y[i]] == 1 and count[a + move_x[i]][b + move_y[i]] > tar + 1:
            queue.append([a + move_x[i], b + move_y[i]])    # 큐 업데이트
            count[a + move_x[i]][b + move_y[i]] = tar + 1   # 지나야 하는 칸 수 업데이트

print(count[n-1][m-1])  # 도착 위치에 도달하기위 한 칸 수 출력