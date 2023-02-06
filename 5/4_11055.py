#시간복잡도 - O(n^2)

n = int(input())    # 수열 크기
arr = list(map(int, input().split()))   # 수열

dp = arr.copy() # 수열 카피

# 모든 수 확인
for i in range(0, n):
    # 이전의 수 확인
    for j in range(0, i):
        # 이전의 수 중 현재 수보다 작고, 그 수까지의 합이 가장 큰 값 저장
        if arr[j] < arr[i] and dp[j] + arr[i] > dp[i]:
            dp[i] = dp[j] + arr[i]
# 가장 큰 값 출력
print(max(dp))