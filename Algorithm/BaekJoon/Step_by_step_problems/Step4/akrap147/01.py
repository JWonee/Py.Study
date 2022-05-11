# 1번 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
Times = int(input())
Number = [int(x) for x in input("").split()]
print(f"{min(Number)} {max(Number)}")
