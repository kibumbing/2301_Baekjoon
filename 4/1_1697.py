from collections import deque

n, k = map(int, input().split())
if n >= k:
    print(n-k)
else:
    deq = deque([])
    visited = set()
    deq.append([n, 0])
    visited.add(n)
    while deq:
        num, count = deq.popleft()
        if num == k:
            break
        if num + 1 < 100001 and num + 1 not in visited:
            deq.append([num + 1, count + 1])
            visited.add(num + 1)
        if num * 2 < 100001 and num * 2 not in visited:
            deq.append([num * 2, count + 1])
            visited.add(num * 2)
        if num - 1 not in visited:
            deq.append([num - 1, count + 1])
            visited.add(num - 1)
    print(deq.popleft()[1])