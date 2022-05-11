# 7번 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

x=int(input())
for i in range(x):
  a,b=map(int,input().split()) ''' a, b에 map 함수를 이용하여 각각을 지정해주었다.'''
  print(f"Case #{i+1}: {a+b}" )
  
# fstring을 사용하는게 가장중요하다
