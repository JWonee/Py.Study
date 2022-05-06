t = int(input('# of test case = ')) #테스트 케이스 개수 정하기

for i in range(1, t+1):  # 1부터 t까지 , i를 사람 기준으로 보기 위해서 범위를 이렇게 설정
    a, b = map(int, input().split()) # i 번째 test case에 들어갈 두 수 a, b 정함
    print("Case #" + str(i) + ':', a+b) #str일때는 붙이려면 + , 다른 타입들 경우 comma
    #print("Case #", i, ':',a+b)