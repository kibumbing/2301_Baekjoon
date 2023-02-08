t = int(input())
ans = []
for _ in range(t):
    k = int(input())
    arr = list(map(int, input().split()))

    d = [0 for _ in range(sum(arr) + 1)]
    for i in arr:
        d[i] = i
    print(d)
    for i in arr:
        for j in range(i, sum(arr) + 1):
            if d[j - i]:
                d[j] += d[j - i] + i
    print(d)