n = int(input())    #수의 개수 입력
arr = map(int, input().split()) #검사할 수 입력

count = 0   #소수의 수
for i in arr:   #모든 수 검사
    prime = 0   #약수의 수
    for j in range(1, i+1): #1부터 검사할 수 사이의 자연수 중
        if i % j == 0:      #검사하는 수의 약수가 있으면
            prime += 1      #약수의 수 1 증가
    if prime == 2:          #약수가 2개인 경우
        count += 1          #소수의 수 1 증가
print(count)                #소수의 수 출력

#시간 복잡도 - O(n^2)
#공간 복잡도 - O(1)