# 12번 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 마지막에 0 0 이라는 input 이 들어온다.
while True:
  a , b = map(int,input().split())
  if a == 0 and b == 0 : ''' if문의 statement에는 오직 True or False만들어 갈 수 있다. and연산자는 True or False 만 반환하므로 사용이 가능하다 '''
    break
# and연산자는 곱 연산자로 둘다 true 이여야만 true값을 반환한다. 즉 a = b = 0 이여야 한다.
# and 대신 &라는 기호를 사용할 수 있다. 
  print(a+b)
