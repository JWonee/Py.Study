# 11번 문제
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

N,X=map(int,input().split())
# N개를 받을 것이고 X보다 작은 숫자를 찾아야 하는 과정이다.
Numbers = list(map(int,(input().split())))
# 내가 받은 숫자를 list로 다시 정리를 하였다. map만으로는 list가 만들어지지 않음
for i in range(N):
  if Numbers[i] < X:
    print(Numbers[i])
#     X보다 작은 element들을 출력시켰다.
