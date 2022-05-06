

print("(0 < A, B < 10)")

t=int(input('#test case = ')) # 테스트 케이스의 갯수 정하기


for i in range(t): # range(1,T+1) 같음
    A,B = map(int,input().split()) # i 번째 테스트 케이스에 두개의 수 A,B 입력
    print(A+B)
