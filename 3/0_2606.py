n = int(input())
m = int(input())
arr = [[0]*n for i in range(n)]
for i in range(m):
     a, b = map(int, input().split())
     arr[a-1][b-1] = 1
     arr[b-1][a-1] = 1

count = 0
queue = []
queue.append(0)
visited = [0]
while len(queue) != 0:
    num = queue[0]
    for i in range(len(arr[num])):
        if arr[num][i] == 1 and (i not in visited):
            queue.append(i)
            visited.append(i)
    queue.pop(0)
    count += 1
print(count-1)

# n = int(input())
# m = int(input())
# arr = [[]for i in range(n)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#     arr[a-1].append(b-1)
#     arr[b-1].append(a-1)
#
# count = 0
# queue = []
# queue.append(0)
# visited = [0]
# while len(queue) != 0:
#     num = queue[0]
#     for i in arr[num]:
#         if i not in visited:
#             queue.append(i)
#             visited.append(i)
#     queue.pop(0)
#     count += 1
# print(count-1)