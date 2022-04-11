# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#  my sol

a,b = input().split()
a = int(a)
b = int(b)
print(a+b)

# 입력값이 한줄에 동시에 출력이 되기 때문에 두개의 입력값을 split하는게 중요하다.
# 여기서 또 의문 굳이 5번6번줄을 쓸 이유가 있을까? a , b = int(input().split())을 사용하면 될줄 알았지만 실패한다. 
# int() argument must be a string a bytes-like object or a number not 'list'라는 구문이 뜬다.
# 즉 int argument 는 string만 가능하다 우리가 split함수가 사용하므로 list가 되었다. 
# 이를 해결하기 위해 map 함수를 사용하면 된다.
# a , b = map(int,input().split())  //  map(적용할 함수, 적용할 값)
