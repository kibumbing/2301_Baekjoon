# 시간복잡도 - O(t*n*price)

t = int(input())    # 테스트 케이스 개수
ans = []
for _ in range(t):
    n = int(input())    # 동전의 가지수
    coins = list(map(int, input().split())) # 동전의 각 금액
    price = int(input())    # 금액

    d = [0 for _ in range(price + 1)]   # 경우의 수 기록
    d[0] = 1    # 하나의 동전으로 금액이 이루어질 경우를 위함

    for coin in coins:  # 모든 동전의 경우 검사
        for i in range(coin, price + 1):    # 동전의 금액보다 큰 모든 금액 검사
            d[i] += d[i - coin]             # 금액에서 동전만큼 뺀 금액의 가능 경우의 수 추가
    ans.append(d[price])                    # 목표 금액의 경우의 수 저장

for i in ans:
    print(i)