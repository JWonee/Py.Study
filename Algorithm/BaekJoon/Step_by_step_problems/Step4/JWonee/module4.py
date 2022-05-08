nums = set() # set: 중복 제거
#처음에 빈 set을 생성할 때는 set( ) 함수를 이용해서 생성해야 한다.
# 집합이 출력될 때는 중괄호 { }에 묶인 값이 출력되는데 nums={ } 형태로 표현하면 딕셔너리 자료형으로 선언되기 때문이다. 
for i in range(10):
    n = int(input('array element ='))
    nums.add(n%42) # 집합에 추가할 때는 add함수, 리스트에 추가할 때는 append

print(len(nums))