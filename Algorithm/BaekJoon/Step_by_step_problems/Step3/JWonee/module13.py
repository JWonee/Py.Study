while True:
    try: #������ �ڵ�
        A,B = map(int,input('A,B=').split())
        print(A+B)
    except: #���ܰ� �߻����� �� ó���ϴ� �ڵ�
        break

    #�ڵ带 �� ���� ������ ��, ������ �����̶� ��Ű���� try except ���� ����ؼ� �����ϴ°� ����.
