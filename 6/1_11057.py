# 시간 복잡도 - O(n)

n = int(input())    # 길이 입력

# 인덱스의 일의 자리는 마지막 숫자, 그 위는 숫자의 길이 - 1 의미
# dp[11] -> 길이 2, 마지막 1
# dp[34] -> 길이 5, 마지막 5
dp = [0 for i in range(10*n)]
# 길이가 1일 때 1로 초기화
for i in range(10):
    dp[i] = 1

# 현재 길이보다 1 작고, 마지막 숫자가 더 적은 경우의 수를 현재 경우에 추가
for i in range(10, 10*n):
    for j in range((i//10-1)*10, (i//10-1)*10+10):
        if i % 10 >= j % 10:
            dp[i] += dp[j]

# 해당 길이의 개수 합
sum = 0
for i in range((n-1)*10, (n-1)*10+10):
    sum += dp[i]
print(sum % 10007)