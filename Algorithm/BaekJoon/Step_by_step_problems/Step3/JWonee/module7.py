t = int(input('# of test case = ')) #�׽�Ʈ ���̽� ���� ���ϱ�

for i in range(1, t+1):  # 1���� t���� , i�� ��� �������� ���� ���ؼ� ������ �̷��� ����
    a, b = map(int, input().split()) # i ��° test case�� �� �� �� a, b ����
    print("Case #" + str(i) + ':', a+b) #str�϶��� ���̷��� + , �ٸ� Ÿ�Ե� ��� comma
    #print("Case #", i, ':',a+b)