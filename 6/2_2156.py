# 시간 복잡도 - O(n)

n = int(input())    # 포도주 잔의 개수
arr = [0 for _ in range(n)] # 포도주의 양
for i in range(n):
    arr[i] = int(input())

# [마신 포도주의 누적 양, 연속으로 마신 횟수] 저장
dp = [[0, 0] for _ in range(n+3)]
nums = set()
# 모든 경우 검사
for i in range(3, n + 3):
    # 연속으로 마시지 않은 경우
    # 전전, 전전전 포도주를 마신 경우의 수 중 포도주 양 max 값 + 현재 포도주의 양
    dp[i][0] = max(dp[i-2][0], dp[i-2][1], dp[i-3][1]) + arr[i - 3]

    # 연속으로 마신 경우
    # 바로 전의 포도주의 연속으로 마시지 않은 경우 누적 양 + 현재 포도주의 양
    dp[i][1] = dp[i-1][0] + arr[i - 3]

    # 둘 중 많은 것 저장
    nums.add(max(dp[i][0], dp[i][1]))

# 최대값 출력
print(max(nums))