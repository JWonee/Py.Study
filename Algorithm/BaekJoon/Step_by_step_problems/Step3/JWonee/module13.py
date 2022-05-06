while True:
    try: #실행할 코드
        A,B = map(int,input('A,B=').split())
        print(A+B)
    except: #예외가 발생했을 때 처리하는 코드
        break

    #코드를 잘 적지 못했을 때, 무조건 실행이라도 시키려면 try except 문을 사용해서 제출하는게 낫다.
