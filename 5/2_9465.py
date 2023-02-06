# 시간복잡도 - O(n*t)

t = int(input())    # 테스트 개수
ans = []

for _ in range(t):
    n = int(input())    # 정수 개수
    arr = []
    for i in range(2):
        arr.append(list(map(int, input().split()))) # 스티커 점수
    dp = [[0]*(n+2) for _ in range(2)]
    # 이전에 떼어낸, 1*1과 1*2 대각선 방향의 스티커 중 큰 점수를 가지는 것에 현재 점수를 더함
    for i in range(2, n + 2):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + arr[0][i - 2]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + arr[1][i - 2]
    ans.append(max(dp[0][n+1], dp[1][n+1]))

for i in range(len(ans)):
    print(ans[i])