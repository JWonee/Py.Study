numbers = []

for i in range(9):
    i = int(input('numbers = '))
    numbers.append(i)

print(max(numbers))
print(numbers.index(max(numbers))+1) #index �Լ��� ����Ʈ�� max�� ��ġ�� ã�� >> 0���� �����ϹǷ� +1