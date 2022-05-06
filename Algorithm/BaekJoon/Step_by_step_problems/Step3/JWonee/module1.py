#N = float(input("N에 대한 구구단 N = ")) #input : 입력할 값에 대한 안내를 출력하고 싶을때 한글로는 에러난다.
N = int(input('N : '))

for i in range(1,10): #1~9
    #range(10) : 0~9
    print(N, '*',i, '=', N*i)
