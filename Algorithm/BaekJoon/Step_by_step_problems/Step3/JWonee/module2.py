

print("(0 < A, B < 10)")

t=int(input('#test case = ')) # �׽�Ʈ ���̽��� ���� ���ϱ�


for i in range(t): # range(1,T+1) ����
    A,B = map(int,input().split()) # i ��° �׽�Ʈ ���̽��� �ΰ��� �� A,B �Է�
    print(A+B)
