# 2번 문제

# 나의 도전
dn_list = []
def d(n):
  Number = n 
  N_list = list(map(int,str(n)))
  while Number < 10000:
    Number = Number +sum(N_list)
    N_list = list(map(int,str(Number)))
    dn_list.append(Number)  
for i in range(10000):
  d(i+1)
lst = list(range(1,10000))

a_sub_b = [x for x in lst if x not in dn_list]
print(a_sub_b)
# 대 실패 

#  Internet code
numbers = list(range(1, 10001))
remove_list = []  # 이후에 삭제할 숫자 list
for num in numbers :
    for n in str(num):
        num += int(n)  # 생성자가 있는 숫자
    if num <= 10000:  # 10,000보다 작거나 같을 때만,
        remove_list.append(num)  # append: 리스트에 요소를 추가할 때
for remove_num in set(remove_list) :  # set 으로 중복값 제거
    numbers.remove(remove_num)
for self_num in numbers :  # 생성자가 있는 숫자를 삭제한 리스트
    print(self_num)
#     
# 아이디어는 비슷하다  모든 경우에 대해 생각하고 여집합으로 빼는 방법.. 근데 잘 안된다 다시 한번 도전해봐야겠다. 
