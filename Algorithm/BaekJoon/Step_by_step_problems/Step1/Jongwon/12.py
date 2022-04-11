# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

a , b , c = input().split()
a = int(a)
b = int(b)
c = int(c)
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)


#  code작성과 별개로 과연 저 식들은 성립할까?
#  증명대상 : (a+b)%c = (a%c+b%c)%c
#  A = kc + n
#  B = k'c + n' 로 치환한다.
#  위 치환식을 좌우에 대입
#  (kc+n + k'c + n')%c = ((kc+n)%c + (k'c+n')%c)%c
#   (k+k') = m 로 정의하고 (XZ + Y)%Z = Y%Z 이므로 (mc + n + n')%c = (n+n')%c 이 성립한다.
# 출처: https://nucleplant.tistory.com/23 [맛있는 데이터]
