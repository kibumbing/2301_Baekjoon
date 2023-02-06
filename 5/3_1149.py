# 시간 복잡도 - O(n)

n = int(input())    # 집의 수
# 각 집을 칠하는 비용
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0]*3 for i in range(n+1)]

# 이전까지 칠한 경우 중 가장 적은 비용에 현재 비용을 더한 값 저장
for i in range(1, n+1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i - 1][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i - 1][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i - 1][2]

print(min(dp[n]))