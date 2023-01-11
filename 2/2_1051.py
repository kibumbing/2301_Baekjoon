n, m = map(int, input().split())    #높이 너비 입력
arr = [[0]*m for i in range(n)]     #배열 생성
for i in range(n):                  #높이만큼 입력 받음
    num = int(input())              #입력
    arr[i][m-1] = num % 10          #1의 자리 수 배열 마지막에 저장
    count = m-2
    #각 자리 수 뒤에서 부터 저장
    while count >= 0:
        num = num//10
        arr[i][count] = num%10
        count -= 1
size = 0    #사이즈 저장
max = min(n, m) #최대 정사각형 변의 길이
for i in range(max+1):  #검사할 정사각형의 변의 길이-1
    for j in range(n-i):    #검사할 정사각형의 왼쪽위 꼭짓점의 x
        for k in range(m-i):     #검사할 정사각형의 왼쪽위 꼭짓점의 y
            if arr[j][k] == arr[j+i][k] == arr[j][k+i] == arr[j+i][k+i]:    #모든 꼭짓점의 값이 같은 경우 size에 크기 저장
                size = (i+1)**2
print(size) #크기 출력

#시간 복잡도 - O(n^3)
#공간 복잡도 - O(n^2)