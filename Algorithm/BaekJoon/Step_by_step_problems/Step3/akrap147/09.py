# 9번 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

x = int(input())
for i in range(x):
  print("*" * (i+1))
#  i+1로 한 이유는 for 구문에서는 i가 0부터 시작하기 때문이다.  
