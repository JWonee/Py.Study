# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
# my_sol

a , b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

# 여기서 핵심은 python은 c와 달리 /의 호환이 잘된다. 즉 float 이든 int든 상관 없이 나누기가 가능하다.
# 몫을 구하기 위해서는 뒤의 소수점을 cut해야한다. 즉 int()를 이용해서 소수점 이하는 버리면 몫이 된다. 

