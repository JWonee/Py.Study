numbers = list(range(1,10_001)) # 10001�� _ �̿����� ������ ���� �� ?
remove_list = []
for num in numbers:
    for n in str(num):
        num += int(n)
    if num <= 10_000:
        remove_list.append(num)

for remove_num in set(remove_list):
    numbers.remove(remove_num) #remove_list�� �ߺ����� set���� ��ȯ�Ͽ�  ���� 

for self_num in numbers:
    print(self_num)