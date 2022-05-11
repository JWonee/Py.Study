while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
# 오류 처리를 사용하면 된다. 계속 input 값을 받다가 어느 순간이 되면 받을 input 값이 없어진다. 그렇게 되면 A,B에 할당되야할 두 정수가 없고 오류가 뜰 것이다.
# 만약 오류가 뜬다면 except로 넘어가 break를 받고 while 구문에 나오게 된다. 
