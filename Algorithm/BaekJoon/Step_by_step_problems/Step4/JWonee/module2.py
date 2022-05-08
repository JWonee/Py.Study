numbers = []

for i in range(9):
    i = int(input('numbers = '))
    numbers.append(i)

print(max(numbers))
print(numbers.index(max(numbers))+1) #index 함수로 리스트의 max의 위치를 찾음 >> 0부터 시작하므로 +1