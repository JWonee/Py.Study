# 4번째 문제
# 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.
# sys.stdin.readline()를 이용해서 푸시오
import sys

t = int(input()) #Test case
for i in range(t):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)

      
      
# import sys 는 무엇을 import하는 것일까?  파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
# sys.stdin.readline().split()는 input()의 느린점을 보완하여 더 빠르게 데이터를 받을 수 있는 방법이다.   
