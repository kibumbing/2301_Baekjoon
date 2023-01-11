arr = [i for i in range(1, 10001)]  #10000까지의 정수 배열에 저장

#생성자로 다음 수 생성
def make_num(num):
    one = num%10    #1의 자리 숫자
    ten = num//10   #10으로 나눴을 때 나머지가 10의 자리 숫자
    hun = ten//10   #10으로 나눴을 때 나머지가 100의 자리 숫자
    tho_one = hun//10   #10으로 나눴을 때 나머지가 1000의 자리 숫자
    tho_ten = tho_one//10   #10으로 나눴을 때 나머지가 10000의 자리 숫자
    return num + one + ten%10 +hun%10 + tho_one%10 + tho_ten%10 #수열의 다음 수 리턴

#모든 수에 대한 셀프 넘버 검사
for i in range(1, 10001):
    num = make_num(i)   #생성자로 다음 수 생성
    while num <= 10000: #10000보다 클 때까지
        arr[num-1] = -1 #함수로 만들어진 수는 -1로 변경
        num = make_num(num)  #생성자로 다음 수 생성

for i in range(10000):
    if arr[i] != -1:    #셀프 넘버일 경우 출력
        print(arr[i])

#시간 복잡도 - O(nlogn)
#공간 복잡도 - O(n)