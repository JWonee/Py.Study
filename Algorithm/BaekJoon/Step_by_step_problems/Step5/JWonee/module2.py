numbers = list(range(1,10_001)) # 10001을 _ 이용하지 않으면 오류 뜸 ?
remove_list = []
for num in numbers:
    for n in str(num):
        num += int(n)
    if num <= 10_000:
        remove_list.append(num)

for remove_num in set(remove_list):
    numbers.remove(remove_num) #remove_list의 중복값을 set으로 변환하여  삭제 

for self_num in numbers:
    print(self_num)