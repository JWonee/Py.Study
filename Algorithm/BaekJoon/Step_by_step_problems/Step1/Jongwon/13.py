# https://www.acmicpc.net/problem/2588
# (세자리 수) * (세자리 수)의 중간 과정을 표현해라 

num1 = int(input())
num2 = input()

for i in range(2, -1, -1):
    print(num1 * int(num2[i]))
print(num1 * int(num2))


# 다른 문제와 달리 입력 예제가 줄이 바뀌어 있어서 헷갈렸다.
# num2의 입력값을 string인 것을 착안해 각각 자리수를 뽑아서 계산했다.
# for loop 안에는 range()를 사용했다. 곱셈은 일의 자리부터 계산하기에 가장 마지막에 있는 num[2]부터 뽑았다.
# range(start, stop, step)이런식으로 사용이 가능하다. 하지만 stop의 마지막 숫자는 범위에 포함이 안되기에 주의해서 사용해야한다. 
