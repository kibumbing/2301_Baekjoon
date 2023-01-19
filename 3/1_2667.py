# 시간 복잡도 - O(n^2)

# 입력
n = int(input())    # 지도의 크기 입력
# 지도 입력
arr = [[0]*(n+2) for i in range(n+2)]
for i in range(1, n+1):
    str = input()
    for j in range(len(str)):
        if str[j] == '1':
            arr[i][j+1] = -1

count = 0   # 총 단지 수
home_count = [] # 각 단지내 집의 수
# 모든 집 탐색
for i in range(1, n+2):
    for j in range(1, n+2):
        if arr[i][j] == -1: # 해당 위치에 집이 있을 경우
            count += 1  # 단지 수 1 증가, 단지 생성
            queue = [[i,j]] # 너비 우선 탐색을 위한 큐
            visited = [[i,j]]   # 방문한 집에 해당 집 포함
            # 너비 우선 탐색 실행
            while len(queue):
                a, b = queue.pop(0) # 검사할 원소 pop
                arr[a][b] = count   # 해당 위치에 단지 입력
                if arr[a-1][b] == -1 and [a-1, b] not in visited:   # 왼쪽 검사
                    queue.append([a - 1, b])
                    visited.append([a - 1, b])
                if arr[a][b - 1] == -1 and [a, b - 1] not in visited: # 윗 집 검사
                    queue.append([a, b - 1])
                    visited.append([a, b - 1])
                if arr[a+1][b] == -1 and [a+1, b] not in visited:   # 오른쪽 집 검사
                    queue.append([a + 1, b])
                    visited.append([a + 1, b])
                if arr[a][b+1] == -1 and [a, b+1] not in visited:   # 아래 집 검사
                    queue.append([a, b + 1])
                    visited.append([a, b + 1])
            home_count.append(len(visited)) # 이웃집 탐색을 통해 얻은 단지 내의 수 저장

print(count)    # 총 단지 수 출력
home_count.sort()   # 각 단지 내 집의 수 정렬
# 각 단지 내 집의 수 출력
for i in range(count):
    print(home_count[i])