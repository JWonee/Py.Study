# 2번 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
N = int(input())
max = N
min = N
tmp = 1
count = 1
for i in range(8):
  N = int(input())
  tmp += 1
  if N > max:
    max = N
    count = tmp

print(max)
print(count)
