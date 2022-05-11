# 구구단
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
x = int(input())
result = 1
for i in range(1,10):
  result = x * i
  print(f"{x} * {i} = {result}")
# fstring을 사용하였다. 
