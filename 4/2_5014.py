from collections import deque

f, s, g, u, d = map(int, input().split())

if (s > g and d < 1) or (s < g and u < 1):
    print("use the stairs")
else:
    deq = deque([])
    deq.append([s, 0])
    visited = set()
    visited.add(s)
    count = 0
    accept = 0
    while deq:
        num, count = deq.popleft()
        if num == g:
            accept = 1
            break
        temp = num + u
        if temp <= f and temp not in visited:
            deq.append([temp, count + 1])
            visited.add(temp)
        temp = num - d
        if temp >= 1 and temp not in visited:
            deq.append([temp, count + 1])
            visited.add(temp)
    if accept == 1:
        print(count)
    else:
        print("use the stairs")