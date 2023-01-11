n = int(input())    # 이동하려는 채널 입력
m = int(input())    # 고장난 버튼 개수 입력
count = 0           # 버튼을 누르는 회수
check_n = n         # 채널 자리수 체크를 위한 변수

if m != 0 and m != 10:  # 고장난 버튼이 없거나, 모두 고장난 경우를 제외
    arr = list(map(int, input().split()))   # 고장난 버튼 입력
    count_down = 0  #++를 통해 채널로 도달할 경우, +버튼을 누르는 횟수
    count_up = 0    #--를 통해 채널로 도달할 경우, -버튼을 누르는 횟수
    n_down = n      #++를 통해 채널로 도달할 경우, 숫자 버튼을 통해 이동할 채널
    n_up = n        #--를 통해 채널로 도달할 경우, 숫자 버튼을 통해 이동할 채널

    while True: # 숫자 버튼을 통해 이동할 채널을 찾을 때까지q
        # ++할 경우
        check_n_down = n_down   # ++하기 전 채널의 자리 숫자 체크를 위한 변수
        out_down = 0            # 모든 자리의 숫자가 입력 가능할 경우 1, 아닐 경우 0
        while check_n_down > 0: # 모든 자리 숫자를 체크하기 전까지
            if check_n_down % 10 in arr:    # 해당 자리의 숫자 버튼이 고장났을 경우
                if n_down > 0:              # 해당 채널이 0보다 클 경우(채널 0ㅇ서 -눌러도 채널은 바뀌지 않음)
                    n_down = n_down - 1     # 해당 채널 - 1
                    count_down = count_down + 1 # +버튼 클릭 횟수 + 1
                out_down = 0                # 적어도 하나의 자리의 숫자가 입력 가능하지 않음
                break
            else:                           # 해당 자리의 숫자 버튼이 고장나지 않았을 경우
                out_down = 1                # 해당 자리의 숫자가 입력 가능 체크
                check_n_down = check_n_down // 10   # 다음 자리 숫자 체크

        # --할 경우
        out_up= 0                           # 모든 자리의 숫자가 입력 가능할 경우 1, 아닐 경우 0
        if n_up == 0 and 0 in arr:          # 해당 채널이 0번이고, 0 버튼이 고장났을 경우
            n_up = n_up + 1                 # 해당 채널 + 1
            count_up = count_up + 1         # -버튼 클릭 횟수 + 1
            out_up = 0                      # 적어도 하나의 자리의 숫자가 입력 가능하지 않음
        check_n_up = n_up                   # --하기 전 채널의 자리 숫자 체크를 위한 변수
        while check_n_up > 0:               # 모든 자리 숫자를 체크하기 전까지
            if check_n_up % 10 in arr:      # 해당 자리의 숫자 버튼이 고장났을 경우
                n_up = n_up + 1             # 해당 채널 + 1
                count_up = count_up + 1     # -버튼 클릭 횟수 + 1
                out_up = 0                  # 적어도 하나의 자리의 숫자가 입력 가능하지 않음
                break
            else:                           # 해당 자리의 숫자 버튼이 고장나지 않았을 경우
                out_up = 1                  # 해당 자리의 숫자가 입력 가능 체크
                check_n_up = check_n_up // 10   # 다음 자리 숫자 체크

        #확인
        # 해당 채널이 0번이고, 0 버튼이 고장나지 않았을 경우
        # ++시 숫자 버튼으로 이동할 채널의 모든 자리의 숫자가 고장나지 않았을 경우
        if (n_down == 0 and 0 not in arr) or out_down == 1:
            check_n = n_down    # 자리수 체크 변수에 저장
            count = count_down  # ++ 버튼 누른 횟수 저장
            break
        # --시 숫자 버튼으로 이동할 채널의 모든 자리의 숫자가 고장나지 않았을 경우
        elif out_up == 1:
            check_n = n_up       # 자리수 체크 변수에 저장
            count = count_up     # -- 버튼 누른 횟수 저장
            break
elif m == 10:   # 고장난 버튼이 10개인 경우
    arr = list(map(int, input().split()))   # 고장난 버튼 입력만 받음

# 해당 수가 0일 경우 0 버튼을 한 번 눌러 이동
if check_n == 0:
    count += 1
else:   # 그외 나머지 자리수 체크해서, 그 수만큼 버튼 누름
    while check_n > 0:
        check_n = check_n // 10
        count += 1

# 숫자와 +/- 조합으로 이동하는 것보다 100에서 +/-로만 이동하는 것이 버튼을 덜 누를 경우
if m == 10 or abs(n-100) < count:
    print(abs(n - 100)) # 100과의 차 출력
else:   # 아닐 경우
    print(count)    # 숫자와 +/- 조합 시 버튼 누른 회수 출력

#시간 복잡도 - O(nlogn)
#공간 복잡도 - O(1)