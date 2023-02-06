# 시간복잡도 - O(n)

# 입력
d, k = map(int, input().split())

# 1: a * 1 + b * 0
# 2: a * 0 + b * 1
arr = [[-1]*2 for i in range(d)]
arr[0][0] = 1
arr[0][1] = 0
arr[1][0] = 0
arr[1][1] = 1

# 3: a * (1 + 0) + b * (0 + 1)
# 5: a * (0 + 1 + 0) + b * (1 + 0 + 1)
# ...
def dp(num, a):
    if arr[num][a] == -1:
        arr[num][a] = dp(num - 1, a) + dp(num - 2, a)
    return arr[num][a]

# 각 a와 b에 곱해질 수를 찾음
a = dp(d-1, 0)
b = dp(d-1, 1)
num = 1
# 1부터 늘려가며 정확히 나누어 떨어지는 a, b를 찾음
while True:
    result = k - a * num
    if result % b == 0:
        print(num)
        print(result // b)
        exit()
    num += 1