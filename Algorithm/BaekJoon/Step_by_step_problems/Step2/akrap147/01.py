# 백준 조건문 1번 문제
# a와b가 임의의 값을 받았을 때 크기 비교 !
# 1330

a , b = map(int,input("").split())
if a > b:
  print(">")
elif a < b:
  print("<")
else:
  print("==")
  
# another sol
A,B = map(int,input().split())

print('>') if A > B else print('<') if A < B else print('==')
#  삼항 연산자를 사용 했다. 생소한 개념이니 알아보겠다.
#  true_value if condition else false_value 
# 첫번째 print('>')를 A>B이면 실행하고 다른 else안에 또다른 삼항연산자가 중첩되어 있다.
# else 안에는 다시 if A<B면 print('<')가 실행이되고 else면 print('==')가 실행이 된다.
