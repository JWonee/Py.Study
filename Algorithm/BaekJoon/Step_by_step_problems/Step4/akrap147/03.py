# 3번 문제
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
a = int(input())
b = int(input())
c = int(input())
# 각각의 숫자를 입력 받는다.
result = str(a * b * c)
# 입력 받은 숫자를 곱하고 string으로 바꾼다.
n_list = list(map(int, str(result)))
# result의 값을 각각 자리수별로 list로 만든다.
Number_count_list = [0 for i in range(0, 10)]
# 0부터 9까지 list를 만든다.
for i in range(len(n_list)):
  Number_count_list[n_list[i]] += 1
# n_list의 i번째 값이 Number_count_list의 위치가 되어 1씩 더한다.
for i in range(len(Number_count_list)):
  print(Number_count_list[i])
