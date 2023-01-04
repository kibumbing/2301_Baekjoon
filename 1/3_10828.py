import sys
input = sys.stdin.readline

#스택 구현
class Stack:
    #리스트로 스택 표현
    def __init__(self):
        self.stack = []
    #push 구현 - 리스트에 정수 추가
    def push(self, num):
        self.stack.append(num)
    #pop 구현
    def pop(self):
        if len(self.stack) == 0:    #스택이 비어있을 경우: -1 출력
            print(-1)
        else:
            print(self.stack.pop()) #스택이 비어있지 않을 경우: 가장 마지막에 입력된 정수 삭제 및 출력
    #size 구현 - 스택의 정수 개수 출력, 리스트의 길이 출력
    def size(self):
        print(len(self.stack))
    #empty 구현
    def empty(self):
        if len(self.stack) == 0:    #스택이 비어있을 경우: 1 출력
            print(1)
        else:                       #스택이 비어있지 않을 경우: 0 출력
            print(0)
    #top 구현
    def top(self):
        if len(self.stack) == 0:    #스택이 비어있을 경우: -1 출력
            print(-1)
        else:
            print(self.stack[len(self.stack)-1])    #가장 마지막에 입력된 정수 출력

stack = Stack()     #스택 객체 생성
n = int(input())    #입력할 명령의 수 입력
arr = [[] for i in range(n)]    #명령을 저장해놓을 배열 n개 생성

#명령 입력 및 저장
for i in range(n):
    arr[i] = input().split()

#명령에 따른 Stack class의 함수 실행
for i in range(n):
    if arr[i][0] == 'push':
        stack.push(int(arr[i][1]))
    elif arr[i][0] == 'pop':
        stack.pop()
    elif arr[i][0] == 'size':
        stack.size()
    elif arr[i][0] == 'empty':
        stack.empty()
    elif arr[i][0] == 'top':
        stack.top()

#시간 복잡도 - O(n)
#공간 복잡도 - O(n)