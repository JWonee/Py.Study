# 백준 조건문 3번 문제
# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

Year = int(input())
if Year % 4 == 0 :
  if Year % 100 == 0:
    if Year % 400 == 0:
      print("1")
    else:
      print("0")
  else:
    print("1")
else:
  print("0") 
  
# another sol
year = int(input())
if ((year%4 == 0)and(year%100 != 0)) or (year%400 == 0):
    print('1')
else:
    print('0')
# and 연산자와 or 연산자를 적적히 섞어서 간단히 표현했다.
# and 연산자는 곱연산 or 연산자는 합 연산이라 생각하면 생각보다 간단하다.
# 4로 나눠지면서 100으로 나눠지면 안되는 경우랑 400으로 나눠지는 경우랑 합연산을 하면 간단하다.
# 참고로 True = nonzero = 1 False = 0

# 삼항연산자 풀이 방법
print('>') if A > B else print('<') if A < B else print('==')
