n = int(input('n ='))

for i in range(n):
    ox_list = list(input('answer list ='))
    score = 0
    sum_score = 0

    for ox in ox_list:
        if ox == 'O':
            score += 1
            sum_score += score
        else:
            score = 0 #���� O�� ������ ���� ���� �� �ʱ�ȭ
    print(sum_score)
    break #�� �� �������� �𸣰ڴ�
